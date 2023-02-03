//
// Copyright (C) 2016 David Eckhoff <david.eckhoff@fau.de>
//
// Documentation for these modules is at http://veins.car2x.org/
//
// SPDX-License-Identifier: GPL-2.0-or-later
//
// This program is free software; you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation; either version 2 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program; if not, write to the Free Software
// Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
//

#include "veins/modules/application/traci/MyVeinsApp.h"
#include "veins/modules/application/traci/TraCIDemo11pMessage_m.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace veins;

Define_Module(veins::MyVeinsApp);

void MyVeinsApp::initialize(int stage)
{
    DemoBaseApplLayer::initialize(stage);
    if (stage == 0) {
        /*
         * When a car is created, loads the color from the colors.csv file.
         * With this approach the car can change different colors during the simulation due to what BST generated the received message
         * Please note that this code creates an istance of colors for every car, this could be more efficient if the colors attribute would be declared static,
         *  but when a static attribute is called veins crashed to me.
         *  I tried so hard to fix that without success and in the end I choose this less efficient but running version.
         *
         * The attribute colors is a 2d vector of string.
         */
        EV << "Initializing " << par("appName").stringValue() << std::endl;
        std::ifstream colorFile;
        std::string line;
        colorFile.open("colors.csv");
        if (colorFile.is_open()){
            while ( std::getline(colorFile,line) ){
                std::stringstream ss(line);
                std::vector<std::string> v; // it's the inner vector. It rappresents a generic line of the .csv file
                while(ss.good()){
                    std::string substr;
                    std::getline(ss, substr, ';');
                    v.push_back(substr);
                }
                colors.push_back(v);
            }
            colorFile.close();
        }

    }
    else if (stage == 1) {
        // Initializing members that require initialized other modules goes here
    }
}

void MyVeinsApp::finish()
{
    DemoBaseApplLayer::finish();
    // statistics recording goes here
}


void MyVeinsApp::onWSM(BaseFrame1609_4* wsm)
{
    TraCIDemo11pMessage* msg = check_and_cast<TraCIDemo11pMessage*>(wsm);
    /*
     * When a car receive a data message, probably it's from a base station, if the data is equal to an id of the BSTs saved on the colors.csv file,
     * the car change its color and save its position on the right file.
     */
    std::ofstream posFile;
    std::string data = msg->getDemoData();
    std::vector<std::string> v;
    // std::string nameFile;
    for (int i=0; i<colors.size(); i++){ // iterate on all the colors (all lines contained in colors.csv)
        v = colors[i];
        if (data == v[0]){
            traciVehicle ->setColor(TraCIColor(stoi(v[1]), stoi(v[2]), stoi(v[3]), 255));
            posFile.open("BST_" + v[0] + ".csv", std::ios_base::app);
            posFile << mobility->getPositionAt(simTime()).x << ";" << mobility->getPositionAt(simTime()).y << std::endl;
            posFile.close();
            scheduleAt(simTime() + 1, new TraCIDemo11pMessage("ComeBackYellow", 14)); // schedule at 1 second after to change back color to yellow
        }
    }
    // Your application has received a data message from another car or RSU
    // code for handling the message goes here, see TraciDemo11p.cc for examples
}

void MyVeinsApp::handleSelfMsg(cMessage* msg)
{
    if (TraCIDemo11pMessage* wsm = dynamic_cast<TraCIDemo11pMessage*>(msg)) {
        if (wsm->getKind() == 14) {
            traciVehicle ->setColor(TraCIColor(255, 255, 0, 255));
            delete (wsm);
        }
    }
    else {
        DemoBaseApplLayer::handleSelfMsg(msg);
    }

    // this method is for self messages (mostly timers)
    // it is important to call the DemoBaseApplLayer function for BSM and WSM transmission
}

void MyVeinsApp::handlePositionUpdate(cObject* obj)
{
    DemoBaseApplLayer::handlePositionUpdate(obj);

    // the vehicle has moved. Code that reacts to new positions goes here.
    // member variables such as currentPosition and currentSpeed are updated in the parent class
}

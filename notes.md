# Problems & Solutions NGN

## Start demo simulation
* start the sumo/veins server:
	* cd in main veins/ directory
	* ./sumo_launchd.py -c sumo-gui
* compile src veins code:
	* cd in main veins/ directory
	* ./configure (only first time)
	* make (to compile everything)
* launch simulation:
	* cd in project directory
	* ./run -u Cmdenv -c WithBeaconing -r 0
		* Note that in some cases the runner is not runnable. To enable it, you have to type in the terminal "chmod +x run" on the project directory.
## Notes about create a personal simulation
### Configuration files
They are files regarding only the pure configuration of the simulation like streets, vehicles, routes of the vehicles, how many BTSs, duration (time) of simulation and etc.
Once modified all these files, saving them is **enough** to see the difference.

PS: Please note that to run the scripts you need to have Sumo installed on your system and you need the access to the Sumo tools directory. We didn't find it so the fastest solution (not the best) is download the scr version of Sumo too. (google "sumo simulator download" and select the source version)

* omnet.ini
	* Config of the omnet simulation
* london.net.xml 
	* Contains information about streets, stoplights, etc
	* netconvert --osm-files london.map.osm -o london.net.xml
	* You can open it (static image) with
		* netedit london.net.xml  
* london.trips.xml
	* Contains a list of trips (so **only** start and finish points) and the id of the vehicle that will travel on that trip
		* Not every trip is valid, the no-valid ones will be not included in *london.rou.xml*
	* python3 *PATH-SUMO*/sumo/tools/randomTrips.py -n london.net.xml -e *DURATION-SIMULATION* -o london.trips.xml -p *PERIOD-SPAWN-CARS*
* london.rou.xml
	* Contains information about all the routes (so start, finish and all what is in between) followed by the id of each car and the time at it will spawn 
	* duarouter -n london.net.xml --route-files london.trips.xml -o london.rou.xml --ignore-errors
		* It's basically a sort of "route algorithm".
		* We guess *--ignore-errors* is necessary for deleting no-valid trips.
* london.poly.xml
	* No needed for Sumo simulation, only for Veins simulation to simulate obstacles for the signal propagation between nodes
	* Adds obstacles like buildings
	* polyconvert --net-file london.net.xml --osm-files london.map.osm -o london.poly.xml
* london.sumo.cfg
	* The only one that has to been manually created (a standard text file) 
	* We copied it from the demo project (*erlangen.sumo.cfg*) and we inserted our config files instead of the demo ones
	* It's a config file for **Sumo** simulator, with "sumo-gui london.sumo.cfg". You can launch a normal Sumo simulation with the net and the routes defined in each files, without the application implemented by Veins (for example: cars follow their trips without changing from their original route planes) 
* london.launchd.xml
	* It's a config file needed for launch the VEINS simulation (so the entire simulation). It indicates to Veins all other Sumo config files, adding  **london.poly.xml** 
	* Like for what we did with *london.sumo.cfg*, we copied from the demo project (erlangen.launchd.xml) and inserted our config files instead of the original ones.

### Application files
They are the veins/omnet++ source code files. They add application and programmable controls at the simulation, like taking decision and changing parameters at run-time if something happens.
You have to compile them like in the demo scenario (it's the same directory and same method).
We worked on *MyVeinsApp.h* and *MyVeinsApp.cc* becouse we didn't want to modify the original source and we didn't find a way to create a personal Application layer with personal name...
* MyVeinsApp.h: standard c++ header file
	* Here you have to declare the MyVeinsApp class with its module and attributes which ereditates from *DemoBaseAppLayer* 
* MyVeinsApp.cc: standard c++ file, here you implement your methods (all based on events)
* Please note that both *MyVeinsApp.h* and *MyVeinsApp.cc* are implemented in namespace veins instead of std: this means that if you want to use anything from the c++ Standard Template Library you have to declare it inline
	* for example: *std::cout<<"Hello World"<<std::endl* instead of *cout<<"Hello World"<<endl*



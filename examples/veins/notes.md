# Problems & Solutions NGN

## Start demo simulation
* start the sumo/veins server:
	* cd in main veins/ directory
	* ./sumo_launchd.py -c sumo-gui
* compile src veins code:
	* cd in main veins/ directory
	* ./configure (only first time)
	* make to compile all the stuffs
* launch simulation:
	* cd in project directory
	* ./run -u Cmdenv -c WithBeaconing -r 0
		* note that in some cases the runner is not runnable, to enable it you have to type in the terminal "chmod +x run" on the project directory
## Notes about create a personal simulation
### Configuration files
They are files regarding only the pure configuration of the simulation like streets, vehicles, routes of the vehicles, how many bst, duration (time) of simulation and etc
Once modified these files save them is **enough** to see the differences

PS: please note that to run the scripts you need sumo installed on your system and you need the access to the sumo tools directory, i didn't find it so the fastest solution i found (sure not the best) is download the scr version of sumo too. (google "sumo simulator download" and select the source version)

* omnet.ini
	* config of the omnet simulation
* seul.net.xml 
	* conteins information about the streets, stoplights, etc
	* netconvert --osm-files seul.map.osm -o seul.net.xml
	* you can open it (static image) with
		* netedit seul.net.xml  
* seul.trips.xml
	* conteins a list of trips (so **only** start and finish points) and the id of the vehicle that will travel on that trip
		* not every trip is valid, the no-valid ones will be not included in *seul.rou.xml*
	* python3 *PATH-SUMO*/sumo/tools/randomTrips.py -n seul.net.xml -e *DURATION-SIMULATION* -o seul.trips.xml -p *PERIOD-SPAWN-CARS*
* seul.rou.xml
	* conteins information about all the routes (so start, finish and all what is in between) followed by the id of each car and the time at it will spawn 
	* duarouter -n seul.net.xml --route-files seul.trips.xml -o seul.rou.xml --ignore-errors
		* it's basicly a sort of "route algorithm"
		* i guess *--ignore-errors* is necessary for delete no-valid trips
* seul.poly.xml
	* no needed for sumo simulation, only for veins simulation to simulate obstacles for the signal propagation between nodes
	* adds obsacles like buildings
	* polyconvert --net-file seul.net.xml --osm-files seul.map.osm -o seul.poly.xml
* seul.sumo.cfg
	* the only one that has to been manually created (a standard text file) 
	* i copied it from the demo project (*erlangen.sumo.cfg*) and i inserted my config files instead of the demo ones
	* it's a config file for **sumo** simulator, with "sumo-gui seul.sumo.cfg" you can launch a normal sumo simulation with the net and the routes defined in respectivly files, without the application implemented by veins (for example: cars follow they trips changing nothing from the original route plane) 
* seul.launchd.xml
	* it's a config file needed for launch VEINS simulation (so the entire simulation), it indicates to veins all other sumo config files, adding  **seul.poly.xml** 
	* like *seul.sumo.cfg*, copied from the demo project (erlangen.launchd.xml) and inserted my config files instead of the original ones

### Application files
They are the source code veins/omnet++ files, they add application and programmable controll at the simulation, like take decision and change parameters at run-time if some events happens.
You have to compile them like in the demo scenario (it's the same directory and same method)
I worked on *MyVeinsApp.h* and *MyVeinsApp.cc* becouse i don't want to modify the original source and i didnt find a way to create a personal Application layer with personal name...
* MyVeinsApp.h: standard c++ header file
	* here you declare the MyVeinsApp class with its module and attributes which ereditates from *DemoBaseAppLayer* 
* MyVeinsApp.cc: standard c++ file, here you implement your method (all based on events)
* please note that both *MyVeinsApp.h* and *MyVeinsApp.cc* are implemented in namespace veins instead of std, this means that if you want to use anything from the c++ Standard Template Library you have to declere it inline
	* for example: *std::cout<<"Hello World"<<std::endl* instead of *cout<<"Hello World"<<endl*



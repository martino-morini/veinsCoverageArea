# STUDY OF mm WAVE COVERAGE AREA IN VEHICULAR NETWORK
This repository contains the demo of a study of mmWave coverage in a vehicular network in a part of London.
This is the project for the "Next Generation Networks" course held by professor Michele Segata in the Università degli Studi di Trento, Italy.
## How to run the demo
### Premise
The demo was developed on a ubuntu machine, it should work well on macOS too, windows is not guaranteed. 
### Requirements
* sumo simulator installed
* veins simulator installed
* omnet++ simulator installed
* this repository itself
### Compile the code
Once you installed all the programs, compile the c++ code, to do that, on a terminal, in the _/veinsCoverageArea_ directory launch _./configure_ and than _make_
### Start the Veins server to work with Sumo
In a terminal, from the _/veinsCoverageArea_ directory, launch _./sumo-launchd,py -c sumo-gui_
### Start the Simulation
In a terminal, from the _/veinsCoverageArea/examples/veins_ directory, launch _./run -u Cmdenv -c WithBeaconing -r 0_
If all gone well, a Sumo Window should opens and the simulation should start. you can pause it, slow it down, and change grafical parameters like every sumo simulation (i suggest you to exagerate the dimension of cars to see them better)
When the simulation ends, the window close itself automaticaly.
### Create the Coverage Area Image
In a terminal, from the _/veinsCoverageArea/examples/veins_ directory,  launch _python plotter.py_.
You should find the _coverageArea.png_ image with the covered points plotted as colored points and BSTs position as colored crosses
### Please note: 
* In some machines you need to specify to use python 3, calling _python3_ instead of _python_
* To guaranteed the success of every script or launcher you need to launch them in their own directory
* The _coverageArea.png_ image is overriden at every _plotter.py_ run, so if you need to save it for any cases, change its name or its position before launch a new run
* The files where the x-y coordinates of the covered points are saved (BST_x.csv) are overriden at every simulation run, so if you need to save it for any cases, change its name or its position before launch a new run
## How to change any parameter of the scenario
### Same map
#### Vehicular parameters
If you need to modify the vehicular parameters, like frequency of spawn of the cars, trips and roads compute by the cars, you need to launch the sumo scripts created for that reasons. More information on the web or in the _notes.md_ conteined in this repository. 
In this demo the simulation last 200 seconds, and a car si spawned every 3 seconds. 
#### Omnet++ Parameters
If you need to change any omnet++ parameters, like the simulation time duration or position of the BSTs, just open the _/veinsCoverageArea/example/veins/omnetpp.ini_ file with a text editor, modify and save it. 
#### Number of BSTs 
If you need to change the number of BSTs in the scenario you need to modify the network, so:
* Open with a text editor the _/veinsCoverageArea/example/veins/RSUExampleScenario.ned_ 
* Change the number of BSTs in the scenario (in the submodules, rsu[x] stands for x BSTs in the scenario)
* make sure to have enough colors saved in _/veinsCoverageArea/example/veins/colors.csv_ file (at least one for every BST)
* If you need to add or modify colors here is a scheme:
	* BST_ID;RED;GREEN;BLUE;PIL_COLOR
	* BST_ID must be equal to the id in omnet++ simulation (0, 1, 2, ...)
	* Note that PIL_COLOR need to be a color defined in the python PIL library:

```python
PIL_COLOR					   : RGB_CODE
aliceblue                      : #f0f8ff
antiquewhite                   : #faebd7
aqua                           : #00ffff
aquamarine                     : #7fffd4
azure                          : #f0ffff
beige                          : #f5f5dc
bisque                         : #ffe4c4
black                          : #000000
blanchedalmond                 : #ffebcd
blue                           : #0000ff
blueviolet                     : #8a2be2
brown                          : #a52a2a
burlywood                      : #deb887
cadetblue                      : #5f9ea0
chartreuse                     : #7fff00
chocolate                      : #d2691e
coral                          : #ff7f50
cornflowerblue                 : #6495ed
cornsilk                       : #fff8dc
crimson                        : #dc143c
cyan                           : #00ffff
darkblue                       : #00008b
darkcyan                       : #008b8b
darkgoldenrod                  : #b8860b
darkgray                       : #a9a9a9
darkgrey                       : #a9a9a9
darkgreen                      : #006400
darkkhaki                      : #bdb76b
darkmagenta                    : #8b008b
darkolivegreen                 : #556b2f
darkorange                     : #ff8c00
darkorchid                     : #9932cc
darkred                        : #8b0000
darksalmon                     : #e9967a
darkseagreen                   : #8fbc8f
darkslateblue                  : #483d8b
darkslategray                  : #2f4f4f
darkslategrey                  : #2f4f4f
darkturquoise                  : #00ced1
darkviolet                     : #9400d3
deeppink                       : #ff1493
deepskyblue                    : #00bfff
dimgray                        : #696969
dimgrey                        : #696969
dodgerblue                     : #1e90ff
firebrick                      : #b22222
floralwhite                    : #fffaf0
forestgreen                    : #228b22
fuchsia                        : #ff00ff
gainsboro                      : #dcdcdc
ghostwhite                     : #f8f8ff
gold                           : #ffd700
goldenrod                      : #daa520
gray                           : #808080
grey                           : #808080
green                          : #008000
greenyellow                    : #adff2f
honeydew                       : #f0fff0
hotpink                        : #ff69b4
indianred                      : #cd5c5c
indigo                         : #4b0082
ivory                          : #fffff0
khaki                          : #f0e68c
lavender                       : #e6e6fa
lavenderblush                  : #fff0f5
lawngreen                      : #7cfc00
lemonchiffon                   : #fffacd
lightblue                      : #add8e6
lightcoral                     : #f08080
lightcyan                      : #e0ffff
lightgoldenrodyellow           : #fafad2
lightgreen                     : #90ee90
lightgray                      : #d3d3d3
lightgrey                      : #d3d3d3
lightpink                      : #ffb6c1
lightsalmon                    : #ffa07a
lightseagreen                  : #20b2aa
lightskyblue                   : #87cefa
lightslategray                 : #778899
lightslategrey                 : #778899
lightsteelblue                 : #b0c4de
lightyellow                    : #ffffe0
lime                           : #00ff00
limegreen                      : #32cd32
linen                          : #faf0e6
magenta                        : #ff00ff
maroon                         : #800000
mediumaquamarine               : #66cdaa
mediumblue                     : #0000cd
mediumorchid                   : #ba55d3
mediumpurple                   : #9370db
mediumseagreen                 : #3cb371
mediumslateblue                : #7b68ee
mediumspringgreen              : #00fa9a
mediumturquoise                : #48d1cc
mediumvioletred                : #c71585
midnightblue                   : #191970
mintcream                      : #f5fffa
mistyrose                      : #ffe4e1
moccasin                       : #ffe4b5
navajowhite                    : #ffdead
navy                           : #000080
oldlace                        : #fdf5e6
olive                          : #808000
olivedrab                      : #6b8e23
orange                         : #ffa500
orangered                      : #ff4500
orchid                         : #da70d6
palegoldenrod                  : #eee8aa
palegreen                      : #98fb98
paleturquoise                  : #afeeee
palevioletred                  : #db7093
papayawhip                     : #ffefd5
peachpuff                      : #ffdab9
peru                           : #cd853f
pink                           : #ffc0cb
plum                           : #dda0dd
powderblue                     : #b0e0e6
purple                         : #800080
rebeccapurple                  : #663399
red                            : (255, 0, 0)
rosybrown                      : #bc8f8f
royalblue                      : #4169e1
saddlebrown                    : #8b4513
salmon                         : #fa8072
sandybrown                     : #f4a460
seagreen                       : #2e8b57
seashell                       : #fff5ee
sienna                         : #a0522d
silver                         : #c0c0c0
skyblue                        : #87ceeb
slateblue                      : #6a5acd
slategray                      : #708090
slategrey                      : #708090
snow                           : #fffafa
springgreen                    : #00ff7f
steelblue                      : #4682b4
tan                            : #d2b48c
teal                           : #008080
thistle                        : #d8bfd8
tomato                         : #ff6347
turquoise                      : #40e0d0
violet                         : #ee82ee
wheat                          : #f5deb3
white                          : (255, 255, 255)
whitesmoke                     : #f5f5f5
yellow                         : #ffff00
yellowgreen                    : #9acd32
```
### Different map
If you want to change map, so you want to change completly scenario you need to create new config files for the veins simulation starting from the .osm (Open Street Map) file which conteins info about streets, obstacles etc. More information on the web or in the _notes.md_ conteined in this repository. 

If you change the map obviosly the plotter script won't work anymore, briefly, here what you have to update it:
* Find a new background image, make sure that its streets are perfectly overlayable to the net used by the simulation. Do to that you can use programs like Adobe Photoshop and a screenshot of the network (you can get it by launch _netedid _x_.net.xml_) or use the screenshot itself as the background
* update the script:
	* update the conversion function from omnetpp 2 image

'''
Author: Martino Morini

The aim of this script is plot the coverage aerea of the BTSs on the original scenario image.
In particular a colored point is plotted for every coordinate x-y where some car has receive a message from a BTS during the veins simulation.
A colored cross is plotted for every BTS, for a better analisys of the coverage area.

To do that, the script takes in input the files "omnetpp.ini" for the BTSs positions, "BTS_x.csv" for the points covered by the BTS number x, and "colors.csv" used to associate a different color for every BTS.

Please note that if you change the names or the position of these files the script must be updated.
'''

from PIL import Image, ImageDraw
import os

def point(draw, x, y, color, delta):
	draw.ellipse((x-delta, y-delta, x+delta, y+delta), fill=color)
	
def cross(draw, x, y, color, r, w):
	draw.line((x-r, y-r) + (x+r, y+r), width=w, fill=color)
	draw.line((x-r, y+r) + (x+r, y-r), width=w, fill=color)
	
def omnt2img(x_in, y_in):
	'''
	Veins coordinates and pixel coordinates are not 1 to 1 convertible.
	If the background image is well choosen a simply moltiplication is enough.
	For more info about change the background image view the project README
	'''
	x_out = float(x_in)*0.6352
	y_out = float(y_in)*0.6352
	
	return (x_out, y_out)


# COLORS LOADING
colors = {} # dictionary where it will be stored the link "BTS id - color" 
clr = open("colors.csv")
clr_line = clr.readline()
while clr_line != "":
	clr_v = clr_line.split(";")
	colors[clr_v[0]] = clr_v[4].strip()
	clr_line = clr.readline()
clr.close()

# IMAGE LOADING
image = Image.open("london.map.png")
draw = ImageDraw.Draw(image)

# FIND OUT BTS FILES
files = os.listdir()
BTSs = []
for file in files:
	if "BTS_" in file:
		BTSs.append(file.split("_")[1].split(".")[0])

BTSs.sort()
print("BTS files found: ", BTSs)

# FIND OUT THE BTS COORDINATES AND PLOT THE BTSs ON THE IMAGE
omn = open("omnetpp.ini")
coordBTS = []

i = 0
o_line = omn.readline()
while o_line != "":
	if ".mobility.x" in o_line:
		coordBTS = []
		for j in range(0, 2):
			app = o_line.split(" ")
			coordBTS.append(app[2].split("\t")[0])
			o_line = omn.readline()
		cBTSi = omnt2img(coordBTS[0], coordBTS[1])
		cross(draw, cBTSi[0], cBTSi[1], colors[str(i)], 6, 4)
			
		i+=1
	else:
		o_line = omn.readline()
		
omn.close()

# PLOT THE POINTS ON THE IMAGE
for BTS in BTSs:
	file = open("BTS_" + BTS + ".csv")
	
	line = file.readline()
	while line != "":
		fcoord = line.split(";")
		coord = omnt2img(fcoord[0], fcoord[1])
		point(draw, coord[0], coord[1], colors[BTS], 2)
		line = file.readline()
	
	file.close()	

image.save("coverageArea.png")


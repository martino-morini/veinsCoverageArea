'''
Author: Martino Morini

The aim of this script is plot the coverage aerea of the BSTs on the original scenario image.
In particular a colored point is plotted for every coordinate x-y where some car has receive a message from a BST during the veins simulation.
A colored cross is plotted for every BST, for a better analisys of the coverage area.

To do that, the script takes in input the files "omnetpp.ini" for the BSTs positions, "BST_x.csv" for the points covered by the BST number x, and "colors.csv" used to associate a different color for every BST.

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
colors = {} # dictionary where it will be stored the link "BST id - color" 
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

# FIND OUT BST FILES
files = os.listdir()
bsts = []
for file in files:
	if "BST_" in file:
		bsts.append(file.split("_")[1].split(".")[0])

bsts.sort()
print("BST files found: ", bsts)

# FIND OUT THE BST COORDINATES AND PLOT THE BSTs ON THE IMAGE
omn = open("omnetpp.ini")
coordBst = []

i = 0
o_line = omn.readline()
while o_line != "":
	if ".mobility.x" in o_line:
		coordBst = []
		for j in range(0, 2):
			app = o_line.split(" ")
			coordBst.append(app[2].split("\t")[0])
			o_line = omn.readline()
		cbsti = omnt2img(coordBst[0], coordBst[1])
		cross(draw, cbsti[0], cbsti[1], colors[str(i)], 6, 4)
			
		i+=1
	else:
		o_line = omn.readline()
		
omn.close()

# PLOT THE POINTS ON THE IMAGE
for bst in bsts:
	file = open("BST_" + bst + ".csv")
	
	line = file.readline()
	while line != "":
		fcoord = line.split(";")
		coord = omnt2img(fcoord[0], fcoord[1])
		point(draw, coord[0], coord[1], colors[bst], 2)
		line = file.readline()
	
	file.close()	

image.save("coverageArea.png")


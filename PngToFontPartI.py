# -*- coding: utf-8 -*-
#PART I 

#This program is broken up into two scripts: 
#One that uses PIL to analyze the pixel data of PNG's
#And another that uses FontForge Scripting tools to build the glyph
#
#Theoretically you should be able to add PIL to FontForge's Python,
#but I couldn't get it to work, so 2 scripts instead of just 1
#
#Tip for using Chinese Characters in Window's command line
#change the code with: chchp 936

#PngToFontPartI:
#This code looks for a file called "fontToCreate"
#and then grabs each PNG file in said folder
#and analyzes each pixel of the image
#
#At the same time it writes the name of the image and the pixel data to a line in data.txt
#Certain file names are not allowed in Windows, <, >,:, ", /, \, |, ?, *, .
#           (Since I use "|" for breaking up the data, I have the next script looking for "rename" when it is the "|" glyph)
#So you'll have to name these file something diffent temporarily
#and rename them in the data.txt file before you run the second script 

from PIL import Image
import os

glyphData = []

class glyph:
    def __init__(self, name, size, data):
        self.name = name
        self.size = size
        self.data = data
    
    def getData(self):
        allData = self.name + "|"
        allData += str(self.size) + "|"
        for b in self.data:
            if b == False:
                allData += "0"
            else:
                allData += "1"
        allData += "\n"
        return allData

def getDataFromFile(fileName):
    img = Image.open("fontToCreate/" + fileName, "r").convert("RGBA")
    px = list(img.getdata())

    imgTwoTone = []
    for pixel in px:
        imgTwoTone.append(bool(pixel[3]))
    glyphOne = glyph(fileName[:(fileName.index("."))], img.size[0], imgTwoTone)
    glyphData.append(glyphOne.getData())
    print(glyphOne.name)


#getting data from all files in the fontToCreate folder
for root, dirs, files in os.walk("./fontToCreate"):
    for filename in files:
        if ".png" in filename:
            getDataFromFile(filename)

#writing data to file
saveFile = open("data.txt", "w", encoding='utf8')
for line in glyphData:
    saveFile.write(line)
saveFile.close()

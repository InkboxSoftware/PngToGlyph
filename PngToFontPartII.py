# -*- coding: utf-8 -*-
#PART II

#Part II requires FontForge's built in Python to work
#So to run this first naviagate to where ffpython.exe is located
#Usually in \whereverYouInstalledFontForge\FontForgeBuilds\bin
#In commandline:
#fontforge -lang=py -script \LocationOfThisScript\PngToFontPartII.py

#PngToFontPartII:
#This code looks for an SFD file in the SfdPath location
#The script opens up the data.txt  file
#And reads each line which represents 1 glyph
#           (If the name "rename" is found in data.txt, this is the "|" glyph)
#It creates or finds the glyph by the line name
#and takes the measurement of the glyph given in data.txt, 
#and fills in each 1 with an appropriately sized square
#and overlap is removed.
#After each line in data.txt is read the .sfd file is saved by the original name.


SfdPath = "C:\\WhereverYourSfdIs\\tmpFontName.sfd"#Path to wherever your SFD file is
SavefontName = "tmpFontName"# should be same .sfd file name

import math
import fontforge
from unicodedata import *
font = fontforge.open(SfdPath)
font.encoding = "UnicodeBmp"



def convertDataToCharGlyph(data, index):
    charBytes = data.split('|')
    char = charBytes[0]
    if char == "rename":
        char = "|"
    print("Designing " + str(index) + ": " + char)
    length = int(charBytes[1])
    i = 0
    x = 0
    y = 0
    c = font.createChar(ord(char), char)
    
    pen = c.glyphPen()
    scale = 1000 / length
    for p in charBytes[2]:
        if bool(int(p)) == False:
            i += 1
            continue
        pen.moveTo(round((x + (i%length)) * scale), round(800-(math.floor(y + (i/length))) * scale))
        pen.lineTo(round(((x + (i%length)) + 1) * scale), round(800-(math.floor(y + (i/length))) * scale))
        pen.lineTo(round(((x + (i%length)) + 1) * scale), round(800-((math.floor(y + (i/length)) + 1)) * scale))
        pen.lineTo(round((x + (i%length)) * scale), round(800-((math.floor(y + (i/length)) + 1)) * scale))
        pen.closePath()
        i += 1
    pen = None
    c.width = 1000
    c.foreground = c.foreground.removeOverlap()


count = 0

glyphFile = open("C:\\Users\\Catba\\Documents\\ARCHIVE\\python\\fontMaker\\data.txt", "r", encoding='utf8')
glyphTextData = glyphFile.readlines()
for glyph in glyphTextData:
    count += 1
    convertDataToCharGlyph(glyph[0:len(glyph)-1], count)


print("Saving File As: " + SavefontName)
font.save("C:\\Users\\Catba\\Documents\\ARCHIVE\\python\\fontMaker\\" + SavefontName + ".sfd")


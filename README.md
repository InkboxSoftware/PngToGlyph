# PngToGlyph
Using FontForge's Scripting tools turn a PNG into a glyph

PNG to Glyph is 2 python scripts that takes PNG files are turns them into glyphs for use in fonts using FontForge's Scripting tools

This program is broken up into two scripts:

One that uses PIL to analyze the pixel data of PNG's

And another that uses FontForge Scripting tools to build the glyph


#PART I 


Theoretically you should be able to add PIL to FontForge's Python, but I couldn't get it to work, so 2 scripts instead of just 1.

Tip for using Chinese Characters in Window's command line, change the code with: chchp 936

PngToFontPartI:

This code looks for a file called "fontToCreate" and then grabs each PNG file in said folder and analyzes each pixel of the image.


At the same time it writes the name of the image and the pixel data to a line in data.txt

Certain file names are not allowed in Windows, <, >,:, ", /, \, |, ?, *, .

           (Since I use "|" for breaking up the data, I have the next script looking for "rename" when it is the "|" glyph)
           
So you'll have to name these file something diffent temporarily and rename them in the data.txt file before you run the second script .



PART II


Part II requires FontForge's built in Python to work

So to run this first naviagate to where ffpython.exe is located

Usually in \whereverYouInstalledFontForge\FontForgeBuilds\bin

In commandline:

fontforge -lang=py -script \LocationOfThisScript\PngToFontPartII.py


PngToFontPartII:

This code looks for an SFD file in the "SfdPath" location.

The script opens up the data.txt file and reads each line which represents 1 glyph.

           (If the name "rename" is found in data.txt, this is the "|" glyph)
           
It creates or finds the glyph by the line name and takes the measurement of the glyph given in data.txt,  and fills in each 1 with an appropriately sized square and then overlap is removed.

After each line in data.txt is read the .sfd file is saved by the original name.


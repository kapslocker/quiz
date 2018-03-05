import Image
from pytesseract import image_to_string
from unidecode import unidecode
import os
import time
import webbrowser

winID = os.popen("xdotool getactivewindow").read()

print "Game Codes: "
print "\t1. LOCO"
print "\t2. BrainBaazi"
print "\t3. Mob Show"
print "\t4. StupidApp"
print "\t5. PrimeTime"

code = int(raw_input("\nEnter game code: "))

if code == 1:
	area = (0,775,1080,950)
	Tarea = (0,575,1080,775)
elif code == 2:
	area = (0,400,1080,625)
	Tarea = (0,200,1080,400)
elif code == 3:
	area = (0,1100,1080,1400)
	Tarea = (0,900,1080,1100)
elif code == 4:
	area = (0,500,1080,725)
	Tarea = (0,320,1080,390)
elif code == 5:
	area = (0,300,1080,725)
	Tarea = (0,320,400,390)
else:
	print "Invalid Code"
	exit()

while 1:
	raw_input("Press Enter to take screenshot")
	start = time.time()

	os.system("adb exec-out screencap -p > screen.png")

	img = Image.open('screen.png')
	cropImg = img.crop(area)

	ques = image_to_string(cropImg,lang='eng')
	ques = unidecode(ques)
#	cropImg.save('crop.png')

	print "Ques: ",ques

	url = "http://google.co.in/search?q={}".format(ques)
	webbrowser.open(url, new=0, autoraise=True)

	imTime = 8
	while (((time.time() - start) < 8) and imTime > 3 ):
#		os.system("adb exec-out screencap -p > screen.png")
		img = Image.open('screen.png')
		cropImg = img.crop(Tarea)
#		imTime = int(image_to_string(cropImg,config='outputbase digits'))
#		cropImg.save('crop.png')

	os.system("xdotool windowactivate "+winID)

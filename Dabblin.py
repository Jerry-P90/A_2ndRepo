import cv2
import tkinter
import numpy
from appJar import gui
app = gui()
app.addLabel("title", "Welcome to appJar")
app.setLabelBg("title", "red")
moarjpeg = cv2.imread('messi5.jpg')
grayjpg = cv2.cvtColor(moarjpeg, cv2.COLOR_BGR2GRAY)
newtemp = cv2.imread('messi_face.jpg' , 0)
w, h = newtemp.shape[::-1]

matched = cv2.matchTemplate(grayjpg, newtemp, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(matched)

top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(moarjpeg,top_left, bottom_right, 255, 2)

#print(moarjpeg)
cv2.imshow('image', moarjpeg)
cv2.waitKey(0)
print(matched)
app.go()
#cv2.imwrite('dark_mess.jpeg', moarjpeg)
#nummies = [4, 5, 6, 82]
#print(nummies)
#m = tkinter.Tk()
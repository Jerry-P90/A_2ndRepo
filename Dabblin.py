import cv2
import numpy as np
import matplotlib.pyplot as plt
from appJar import gui
import tkinter as Tk

#OpenCV
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
cv2.waitKey(2000)
cv2.destroyAllWindows()
print(matched)

#ORB Matching

img1 = cv2.imread('brick_house.jpg', 0)
img2 = cv2.imread('brick.jpg', 0)
orb = cv2.ORB_create()
kp1, desc1 = orb.detectAndCompute(img1,None)
kp2, desc2 = orb.detectAndCompute(img2,None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(desc1,desc2)
matches = sorted(matches, key = lambda x:x.distance)
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:20],None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
plt.imshow(img3),plt.show()

#AppJar

app = gui("Login Window", "400x200")
app.addLabel("title", "AppJar Testing")
app.setBg("light blue")
app.setLabelBg("title", "white")
#app.addLabelEntry("Username")
#app.addLabelSecretEntry("Password")
#def press(button):
#    if button == "Cancel":
#        app.stop()
#    else:
#        usr = app.getEntry("Username")
#        pwd = app.getEntry("Password")
#        print("User:", usr, "Pass:", pwd)
#app.addButtons(["Submit", "Cancel"], press)
#app.addButton("Insert image", press)
#app.setBgImage('think_spin.gif')
def press(button):
    if button == "Match Images":
        moarjpeg = cv2.imread('messi5.jpg')
        grayjpg = cv2.cvtColor(moarjpeg, cv2.COLOR_BGR2GRAY)
        newtemp = cv2.imread('messi_face.jpg', 0)
        w, h = newtemp.shape[::-1]
        matched = cv2.matchTemplate(grayjpg, newtemp, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(matched)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(moarjpeg, top_left, bottom_right, 255, 2)
        # print(moarjpeg)
        cv2.imshow('image', moarjpeg)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()
        print(matched)
        app.stop()
app.addButton("Match Images", press)
app.addWebLink("View the code", "https://github.com/Jerry-P90/A_2ndRepo/blob/master/Dabblin.py")
app.go()
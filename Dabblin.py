import cv2
import numpy as np
import matplotlib.pyplot as plt
from appJar import gui
import tkinter as Tk
from tkinter import *

#Template Matching
#moarjpeg = cv2.imread('messi5.jpg')
#grayjpg = cv2.cvtColor(moarjpeg, cv2.COLOR_BGR2GRAY)
#newtemp = cv2.imread('messi_face.jpg' , 0)
#w, h = newtemp.shape[::-1]
#matched = cv2.matchTemplate(grayjpg, newtemp, cv2.TM_CCOEFF_NORMED)
#min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(matched)
#top_left = max_loc
#bottom_right = (top_left[0] + w, top_left[1] + h)
#cv2.rectangle(moarjpeg,top_left, bottom_right, 255, 2)
#cv2.imshow('image', moarjpeg)
#cv2.waitKey(2000)
#cv2.destroyAllWindows()
#print(matched)

#Multi template matching
#img_rgb = cv2.imread('brick_house.jpg')
#img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
#template = cv2.imread('brick.png',0)
#w, h = template.shape[::-1]
#res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
#threshold = 0.8
#loc = np.where( res >= threshold)
#for pt in zip(*loc[::-1]):
#    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
#cv2.imshow('res.png',img_rgb)
#print(res)

#Feature Matching
#img1 = cv2.imread('brick_house.jpg', 0)
#img2 = cv2.imread('brick.png', 0)
#orb = cv2.ORB_create()
#kp1, desc1 = orb.detectAndCompute(img1,None)
#kp2, desc2 = orb.detectAndCompute(img2,None)
#bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
#matches = bf.match(desc1,desc2)
#matches = sorted(matches, key = lambda x:x.distance)
#img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
#plt.imshow(img3),plt.show()

#AppJar
app = gui("AppJar Testing", "800x600")
app.addLabel("title", "AppJar Testing")
app.setBg("light blue")
app.setLabelBg("title", "white")
def press(button):
    if button == "Image Matching":
        moarjpeg = cv2.imread('messi5.jpg')
        grayjpg = cv2.cvtColor(moarjpeg, cv2.COLOR_BGR2GRAY)
        newtemp = cv2.imread('messi_face.jpg', 0)
        w, h = newtemp.shape[::-1]
        matched = cv2.matchTemplate(grayjpg, newtemp, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(matched)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(moarjpeg, top_left, bottom_right, 255, 2)
        cv2.imshow('image', moarjpeg)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()
        #print(matched)
    elif button == "Feature Matching":
        img1 = cv2.imread('brick_house.jpg', 0)
        img2 = cv2.imread('brick_wall.jpg', 0)
        orb = cv2.ORB_create()
        kp1, desc1 = orb.detectAndCompute(img1, None)
        kp2, desc2 = orb.detectAndCompute(img2, None)
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(desc1, desc2)
        matches = sorted(matches, key=lambda x: x.distance)
        img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None,
                               flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
        plt.imshow(img3), plt.show()
    elif button == "Input Image":
        root=Tk()
        root.filename = filedialog.askopenfilename(initialdir="/gui/images", title="Select a file", filetypes=(("png files", "*.png"),("all files", "*.*")))

        Tk().withdraw()
        filename = filedialog.askopenfilename(filetypes=(("C:\Users\S1840085\Pictures\Rando trash",".jpg",".png",".jpeg")))
        print(filename)
    elif button == "Close Program":
        app.stop()
app.addButton("Image Matching", press)
app.addButton("Feature Matching", press)
app.addButton("Input Image", press)
app.addButton("Close Program", press)
app.addWebLink("View the code", "https://github.com/Jerry-P90/A_2ndRepo/blob/master/Dabblin.py")
app.go()
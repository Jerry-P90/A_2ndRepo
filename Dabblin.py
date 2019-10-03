import cv2
import tkinter
import numpy
moarjpeg = cv2.imread('messi5.jpg')
grayjpg = cv2.cvtColor(moarjpeg, cv2.COLOR_BGR2GRAY)
newtemp = cv2.imread('messi_face.jpg' , 0)
matched = cv2.matchTemplate(grayjpg, newtemp, cv2.TM_CCOEFF_NORMED)
#print(moarjpeg)
cv2.imshow('image', moarjpeg)
cv2.waitKey(2000)
print(matched)
#cv2.imwrite('dark_mess.jpeg', moarjpeg)
#nummies = [4, 5, 6, 82]
#print(nummies)
#m = tkinter.Tk()
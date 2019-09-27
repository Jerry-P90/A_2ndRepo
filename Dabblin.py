import cv2
import tkinter
moarjpeg = cv2.imread('messi5.jpg' , 0)
print(moarjpeg)
cv2.imshow('image', moarjpeg)
cv2.waitKey(2000)
cv2.imwrite('dark_mess.jpeg', moarjpeg)
nummies = [4, 5, 6, 82]
print(nummies)
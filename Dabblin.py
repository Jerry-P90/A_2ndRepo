import cv2
moarjpeg = cv2.imread('messi5.jpg' , 0)
print(moarjpeg)
cv2.imshow('image', moarjpeg)
cv2.waitKey(5000)
cv2.imwrite('dark_mess.jpeg', moarjpeg)
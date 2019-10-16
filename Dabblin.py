import cv2
import numpy
from appJar import gui

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

#AppJar
app = gui("Login Window", "400x200")
app.addLabel("title", "AppJar Testing")
app.setBg("light blue")
app.setLabelBg("title", "white")
app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")
def press(button):
    if button == "Cancel":
        app.stop()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        print("User:", usr, "Pass:", pwd)
app.addButtons(["Submit", "Cancel"], press)
app.addButton("Insert image", press)
app.addWebLink("View the code", "https://github.com/Jerry-P90/A_2ndRepo/blob/master/Dabblin.py")
app.go()
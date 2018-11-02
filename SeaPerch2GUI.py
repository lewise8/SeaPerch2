# Import required libraries
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
# import cv2
# import PIL.Image, PIL.ImageTk
# from skimage import data, io, filters
# import numpy
# import RPi.GPIO as GPIO
import time

# Set up the board mode for output
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(7, GPIO.OUT)

top = Tk()
top.geometry("2000x1000")

# Set up panes
ControllerWindow = PanedWindow()
ControllerWindow.pack(fill=BOTH, expand=1)

RawImage = PanedWindow(ControllerWindow, orient=VERTICAL)
ControllerWindow.add(RawImage)

top = Label(RawImage, text="Raw Image")
RawImage.add(top)

bottom = Label(RawImage, text="Processed Image")
RawImage.add(bottom)


# Define Commands for the buttons
def LeftCommand():
   msg = messagebox.showinfo( "", "Go Left")

def RightCommand():
   msg = messagebox.showinfo( "", "Go Right")

def ForwardCommand():
   msg = messagebox.showinfo( "", "Go Forward")

def BackCommand():
   msg = messagebox.showinfo( "", "Go Backwards")

def StopCommand():
   msg = messagebox.showinfo( "", "Stahp!")

def KillCommand():
   msg = messagebox.showinfo( "", "Sub Is Now Dead")

def UpCommand():
   msg = messagebox.showinfo( "", "Go Up")

def DownCommand():
   msg = messagebox.showinfo( "", "Go Down")


LeftButton = Button(ControllerWindow, text = "Left")
LeftButton.place(x = 50,y = 300)
#LeftButton.bind('<ButtonPress-1>', LeftCommand())
#LeftButton.bind('<ButtonRelease-1>', LeftCommand())

#LeftButton = Button(ControllerWindow, text = "Left", command = GPIO.output(7,True))
#LeftButton.place(x = 50,y = 300)

RightButton = Button(ControllerWindow, text = "Right", command = RightCommand)
RightButton.place(x = 300,y = 300)

ForwardButton = Button(ControllerWindow, text = "Forward", command = ForwardCommand)
ForwardButton.place(x = 180,y = 200)

BackwardsButton = Button(ControllerWindow, text = "Backwards", command = BackCommand)
BackwardsButton.place(x = 170,y = 400)

StopButton = Button(ControllerWindow, text = "Stahp", command = StopCommand)
StopButton.place(x = 170,y = 300)

KillButton = Button(ControllerWindow, text = "Kill", command = KillCommand)
KillButton.place(x = 170,y = 600)

UpButton = Button(ControllerWindow, text = "Up", command = UpCommand)
UpButton.place(x = 50,y = 50)

DownButton = Button(ControllerWindow, text = "Down", command = DownCommand)
DownButton.place(x = 50,y = 100)

KillButton.config(fg='Red')

# Working on camera from here on------------
# cap = cv2.VideoCapture(0)


ControllerWindow.mainloop() 

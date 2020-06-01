import cv2
import numpy as np 
import math
import cmath
from tkinter import Tk
from tkinter.filedialog import askopenfilename
W =1000


def addition(img, img1):
    img = cv2.imread(img)
    nimg1 = cv2.imread(img1)
    height, width, depth = img.shape
    img1 = cv2.resize(nimg1,(int(width),int(height)))
    print (img.shape)
    print (img1.shape)
    
    for y in range(0,width):
    	for x in range(0,height):
    	    img[x,y,0] = img[x,y,0]/2+img1[x,y,0]/2
    	    img[x,y,1] = img[x,y,1]/2+img1[x,y,1]/2
    	    img[x,y,2] = img[x,y,2]/2+img1[x,y,2]/2
    cv2.imshow('Coverted Image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def sustraction(img, img1):
    img = cv2.imread(img)
    nimg1 = cv2.imread(img1)
    height, width, depth = img.shape
    img1 = cv2.resize(nimg1,(int(width),int(height)))
    for y in range(0,width):
    	for x in range(0,height):
    	    c1=int(img[x,y,0])-int(img1[x,y,0])
    	    c2=int(img[x,y,1])-int(img1[x,y,1])
    	    c3=int(img[x,y,2])-int(img1[x,y,2])
    	    if(c1<0 and c2<0 and c3<0):
    	        c1,c2,c3 = 0,0,0
    	    elif(c1>255 and c2>255 and c3>255):
    	        c1,c2,c3 = 255,255,255
    	    img[x,y,0] = c1
    	    img[x,y,1] = c2
    	    img[x,y,2] = c3
    	    
    cv2.imshow('Coverted Img',img)
    cv2.waitKey(0)    
    cv2.destroyAllWindows()


Tk().withdraw()
filename = askopenfilename()
filename1 = askopenfilename()

sustraction(filename,filename1)

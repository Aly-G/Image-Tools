import tkinter
import cv2
from cv2 import resize
import numpy
import PIL
#funtions
def showImage():
    img=cv2.imread("sample.jpg")
    cv2.imshow('Unmodified Image', img)
def greyscale():
    img=cv2.imread("sample.jpg", 0)
    cv2.imshow('Greyscale Image', img)
def applyWatermark():
    img=cv2.imread("sample.jpg")
    textin=input("What text do you want to watermark onto the image?: ")
    text=cv2.putText(img, textin, (500,550), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 2)
    cv2.imshow('Watermarked Image', img)
def invert():
    img=cv2.imread("sample.jpg")
    inverted=cv2.bitwise_not(img)
    cv2.imshow('Inverted Image', inverted)
def enhance():
    img=cv2.imread("sample.jpg")
    img_enh=cv2.equalizeHist(img)
    cv2.imshow('Enhanced Image', img_enh)
def doResize():
    img=cv2.imread("sample.jpg")
    width=int(input("Enter the desired width (in pixels) of your image: "))
    height=int(input("Enter the desired height (in pixels) of your image: "))
    widthheight=(width, height)
    resized=cv2.resize(img, widthheight, interpolation=cv2.INTER_LINEAR)
    cv2.imshow('Resized Image', resized)
def countPixels():
    pixel=str(img.size)
    window=tkinter.Tk()
    text=tkinter.Text(window)
    text.insert(tkinter.INSERT, pixel)
    text.pack()
#main code
print("NOTICE: On the online version of this code, a sample image can only be used. Download the code from <github link> to use a custom image by replacing sample.jpg with your own image renamed to be sample.jpg")
img=cv2.imread("sample.jpg")
window=tkinter.Tk()
showimg=tkinter.Button(window, text="Show Unmodified Image", command=showImage) #show umodified image
grey=tkinter.Button(window, text="Show Image in Greyscale", command=greyscale) #show image in greyscale
watermark=tkinter.Button(window, text="Apply Watermark", command=applyWatermark) #apply watermark
inverted=tkinter.Button(window, text="Invert Colours", command=invert)
resize=tkinter.Button(window, text="Resize your image", command=doResize)
pixels=tkinter.Button(window, text="Count total pixels", command=countPixels)
showimg.pack()
grey.pack()
watermark.pack()
inverted.pack()
resize.pack()
pixels.pack()
window.mainloop()
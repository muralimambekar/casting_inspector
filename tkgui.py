#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 10:31:19 2020

@author: murali
"""
from tkinter import *
from keras.preprocessing import image
import numpy as np
from keras.models import load_model
# loading Python Imaging Library 
from PIL import ImageTk, Image   
# To get the dialog box to open when required  
from tkinter import filedialog 

model = load_model('vggmodel.h5')
print('Model Loaded Sucessfully')
     
def open_img(): 
    # Select the Imagename  from a folder  
    x = openfilename() 
    # opens the image 
    img = Image.open(x) 
    im1 = img.save("casting.jpeg")
    img = ImageTk.PhotoImage(img) 
    # create a label 
    panel = Label(root, image = img)   
    # set the image as img  
    panel.image = img 
    panel.place(bordermode=OUTSIDE, x=50, y=50)
       
    
def openfilename(): 
  
    # open file dialog box to select image 
    # The dialogue box has a title "Open" 
    filename = filedialog.askopenfilename(title ='Select Image') 
    return filename 

def prediction():
    img ="casting.jpeg"    
    test_image = image.load_img(img, target_size = (300, 300))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = model.predict(test_image)
    
    if result[0][0] == 1:
        prediction = 'CASTING IS OK         '
        
    else:
        prediction = 'CASTING IS DEFECTIVE'
        
    result = Label(root, text = prediction)   
    # set the image as img  
    result.place(bordermode=OUTSIDE, x=400, y=120)

# Create a window 
root = Tk()   
# Set Title as Image Loader 
root.title("CASTING INSPECTOR")   
# Set the resolution of window 
root.geometry("700x450")   
# Do't Allow Window to be resizable 
root.resizable(width = False, height = False)   
# Create a button and place it into the window using place layout 
btn_open_image = Button(root, text ='Open image', command = open_img).place( 
                                        x = 10, y= 400) 
btn_predict = Button(root, text ='Predict', command = prediction).place( 
                                        x = 200, y= 400) 
result_hd = Label(root, text = "RESULT")
result_hd.place(bordermode=OUTSIDE, x=400, y=90)
root.mainloop() 

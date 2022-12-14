from imgaug import augmenters as iaa
#* **********************************************
#Code for pulling images into a 4d numpy array * **********************************************
import os 
import sys
import numpy as np 
import matplotlib.pyplot as plt 
import glob 
import pickle 
import cv2 
import imageio

images = [] 
for image_fp in glob.glob ("/Users/saimkhalid/Documents/iOPTIME Resources/Tuber Dataset/Data_Augmentation/original/*.png"):
    image = cv2.imread(image_fp) [:, :, : :-1]
    images.append(image)
images = np.array(images)

print ('Images Pulled')
#seq = iaa. Sequential ([iaa. Fliplr (0.5), iaa. Dropout ( (0, . 2) ) ])
#seq. show_grid (images [0], cols=3, rows=3)
#Augment 10 times the initial image 
#Zoom in on all images by a factor of 2.
images_aug = iaa.Affine(scale=(0.5, 1.5)).augment_images(images)
#images_aug = iaa.Affine (scale=(1.2)).augment_images(images)
# iterate over every example image and save it to 0.jpg, 1. jpg, 2.jpg, ... for i, 
for i, image_aug in enumerate (images_aug):
    cv2.imwrite ( "/Users/saimkhalid/Documents/iOPTIME Resources/Tuber Dataset/Data_Augmentation/Augmented_dataset/%d.png" % (i, ), image_aug)


import numpy
import cv2


frame = cv2.imread(r"C:\Users\vigne\Desktop\automatic-toll-management\test_images\2.jpg")
x,y,w,h = 
crop_img = frame[y:y + h, x:x + w]
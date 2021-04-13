import numpy
import cv2


frame = cv2.imread(r"C:\Users\vigne\Desktop\automatic-toll-management\test_images\2.jpg")
x,y,w,h = [291,853,189, 65]
crop_img = frame[y:y + h, x:x + w]
cv2.imwrite(r"C:\Users\vigne\Desktop\test.jpg", crop_img)
import os
import cv2
pathOut = '/home/vigneshdesmond/Desktop/video2frames'
count = 0
counter = 1
listing = os.listdir('/home/vigneshdesmond/Desktop/videos')
for vid in listing:
    vid = r"C:/Users/Me/videos/train/"+vid
    cap = cv2.VideoCapture(vid)
    count = 0
    counter += 1
    success = True
    while success:
        success,image = cap.read()
        print('Read a new frame:',success)
        if count%30 == 0 :
             cv2.imwrite(pathOut + 'video%d'%counter + 'frame%d.jpg'%count ,image)
        count+=1
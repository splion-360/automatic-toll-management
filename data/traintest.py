import glob
import os
# Images directory
current_dir = '/home/vigneshdesmond/darknet/data/Images'
# Percentage of images to be used for the valid set
percentage_test = 10
# if exists delete train test
os.remove('/home/vigneshdesmond/darknet/data/train.txt')
os.remove('/home/vigneshdesmond/darknet/data/test.txt')
# Create train.txt and valid.txt
file_train = open('/home/vigneshdesmond/darknet/data/train.txt', 'w')  
file_test = open('/home/vigneshdesmond/darknet/data/test.txt', 'w')
# Populate train.txt and valid.txt
counter = 1  
index_test = round(100 / percentage_test)  
for file in glob.iglob(os.path.join(current_dir, '*.jpg')):  
    title, ext = os.path.splitext(os.path.basename(file))
    if counter == index_test:
        counter = 1
        file_test.write(current_dir + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(current_dir + "/" + title + '.jpg' + "\n")
        counter = counter + 1
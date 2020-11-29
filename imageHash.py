from PIL import Image
import imagehash
dw1 = imagehash.average_hash(Image.open('/home/vigneshdesmond/darknet/imgs-all/imgs/000019_2928289.jpg')) 
dw2 = imagehash.average_hash(Image.open('/home/vigneshdesmond/darknet/imgs-all/imgs/000002_2850283.jpg')) 
w1 = imagehash.average_hash(Image.open('/home/vigneshdesmond/darknet/imgs-all/imgs/000005_2864184.jpg')) 
ga1 = imagehash.average_hash(Image.open('/home/vigneshdesmond/darknet/imgs-all/imgs/000013_2900860.jpg')) 
cutoff = 5

# if hash0 - hash1 < cutoff:
#   print('images are similar')
# else:
#   print('images are not similar')

print(dw1-dw2)
print(dw1 - w1)
print(dw1- ga1)
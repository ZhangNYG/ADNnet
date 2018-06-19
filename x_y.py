from PIL import Image
from pylab import *

im = array(Image.open('E:\\tmp\ADN\FIRESET\FIRST\\fire\\0001.jpg'))
imshow(im)
print('Please click 2 points')

x = ginput(2)
print('you clicked:', x)
print(x[0][0],x[0][1],-x[0][0]+x[1][0],-x[0][1]+x[1][1])


show()
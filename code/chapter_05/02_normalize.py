# example of pixel normalization
from PIL import Image
from numpy import asarray

#load image
img = Image.open('sydney_bridge.jpg')
pixels = asarray(img)

#check data
print("Pixels datatype: %s" % pixels.dtype)
print('Pixels max: %f, Pixels min: %.f' % (pixels.min(), pixels.max()))

#convert to floats
pixels = pixels.astype('float32')
print("Pixels datatype: %s" % pixels.dtype)

#normalize
pixels = pixels/255
print('Pixels max: %.3f, Pixels min: %.3f' % (pixels.min(), pixels.max()))

img.show()
from PIL import Image
import os
import color


class PixelArray(object):

  def __init__(self, size, pixels):
    self.size = size
    self._pixels = pixels
  
  def __getitem__(self, index):
    assert type(index) is tuple and len(index) == 2, 'Index must be an x,y tuple'
    x, y = index
    width, height = self.size
    assert x < width, 'x must be less than width %s' % (x, width)
    assert y < height, 'y must be less than width %s' % (y, height)
    
    return self._pixels[x][y]

def GetPixelArrayFromImage(img):
  width, height = img.size

  image_pixels = img.load()

  pixels = list()
  for x in xrange(width): 
    pixel_column = list()
    for y in xrange(height):
      pixel = image_pixels[x,y]
      pixel_color = color.RGBColor(pixel[0], pixel[1], pixel[2])
      pixel_column.append(pixel_color)
    pixels.append(pixel_column)

  size = (width, height)
  return PixelArray(size, pixels)

def IterateOverPixelArray(pixel_array):
  for x in xrange(pixel_array.size[0]):
    for y in xrange(pixel_array.size[1]):
      yield (x,y), pixel_array[x,y]
      

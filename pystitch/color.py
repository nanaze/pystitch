import math
import re

def _check_8int(val):
  if not (0 <= val <= 255):
    raise ValueError('Value must be 0-255', val)


class RGBColor(object):

  def __init__(self, red, green, blue):
    _check_8int(red)
    _check_8int(green)
    _check_8int(blue)

    self._red = red
    self._green = green
    self._blue = blue

  @property
  def red(self):
    return self._red

  @property
  def green(self):
    return self._green

  @property
  def blue(self):
    return self._blue

  def __eq__(self, other):
    return (
      (self.red == other.red) and
      (self.green == other.green) and
      (self.blue == other.blue))

  @staticmethod
  def distance(color1, color2):
    return math.sqrt(
      (color1.red - color2.red) ** 2 +
      (color1.green - color2.green) ** 2 +
      (color1.blue - color2.blue) ** 2
      )

def _HexToInt(str):
  return int('0x%s' % str, 16)

def RGBColorFromHexString(str):
  match = re.match(r'^#?([0-9A-Fa-f]{6})$', str)
  if match:
    color = match.group(1)
    assert len(color) == 6
    return RGBColor(
      _HexToInt(color[0:2]),
      _HexToInt(color[2:4]),
      _HexToInt(color[4:6]))

  raise ValueError('Not valid hex color %s' % str)
      
    
  

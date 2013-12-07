import math
import re

def _check_8int(val):
  if type(val) is not int:
    raise ValueError('Value must be an integer', val)
  if not (0 <= val <= 255):
    raise ValueError('Value must be 0-255', val)


class RGBColor(object):

  def __init__(self, red, green, blue):
    _check_8int(red)
    _check_8int(green)
    _check_8int(blue)

    self.red = red
    self.green = green
    self.blue = blue

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

  def __str__(self):
    return super(RGBColor, self).__str__() + str((self.red, self.green, self.blue))

def _HexToInt(str):
  return int('0x%s' % str, 16)

def RGBColorFromHexString(hex_str):
  red, green, blue = RGBTupleFromHexString(hex_str)
  return RGBColor(red, green, blue)

def RGBTupleFromHexString(hex_str):
  match = re.match(r'^#?([0-9A-Fa-f]{6})$', hex_str)
  if match:
    color = match.group(1)
    assert len(color) == 6
    return (
      _HexToInt(color[0:2]),
      _HexToInt(color[2:4]),
      _HexToInt(color[4:6]))

  raise ValueError('Not valid hex color %s' % str)

      
    
  

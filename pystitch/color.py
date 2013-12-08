import math
import re

def _check_8int(val):
  if type(val) is not int:
    raise ValueError('Value must be an integer', val)
  if not (0 <= val <= 255):
    raise ValueError('Value must be 0-255', val)


class RGBColor(tuple):

  def __new__(cls, red, green, blue):
    t = tuple.__new__(cls, [red, green, blue])                                        
    # Assert valid values
    for val in t:
      _check_8int(val)

    return t

  @property
  def red(self):
    return self[0]

  @property
  def green(self):
    return self[1]

  @property
  def blue(self):
    return self[2]

  @staticmethod
  def distance(color1, color2):
    return math.sqrt(
      (color1[0] - color2[0]) ** 2 +
      (color1[1] - color2[1]) ** 2 +
      (color1[2] - color2[2]) ** 2
      )

def _HexToInt(str):
  return int('0x%s' % str, 16)

def RGBColorFromHexString(hex_str):
  match = re.match(r'^#?([0-9A-Fa-f]{6})$', hex_str)
  if match:
    color = match.group(1)
    assert len(color) == 6
    return RGBColor(
      _HexToInt(color[0:2]),
      _HexToInt(color[2:4]),
      _HexToInt(color[4:6]))

  raise ValueError('Not valid hex color %s' % str)

      
    
  

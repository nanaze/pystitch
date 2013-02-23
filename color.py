import math

def _check_8int(val):
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
    

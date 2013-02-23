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

class RGBColor(tuple):

  def __new__(cls, red, green, blue): 
    return tuple.__new__(cls, [red, green, blue])                                        
  @property
  def red(self):
    return self[0]

  @property
  def green(self):
    return self[1]

  @property
  def blue(self):
    return self[2]

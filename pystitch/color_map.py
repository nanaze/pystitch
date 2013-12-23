
class ColorMap(object):

  def __init__(self):
    self._color_map = dict()
    self._offset = 0

  def get(self, color):
    if color not in self._color_map:
      self._color_map[color] = chr(ord('A') + self._offset)
      self._offset += 1

    return self._color_map[color]

  def __iter__(self):
    items = self._color_map.items()
    for key, val in items:
      yield key, val

import csv
import os
import color

def _GetDataDirPath():
  return os.path.join(os.path.dirname(__file__), 'data')

def _GetCsvPath():
  return os.path.join(_GetDataDirPath(), 'dmccolors.csv')

def _GetCsvString():
  with open(_GetCsvPath()) as f:
    return f.read().strip()

def _CreateDmcColorFromRow(row):
  number = int(row[0])
  name = row[1]
  hex_color = row[5]
  rgb_color = color.RGBColorFromHexString(hex_color)
  return DMCColor(number, name, rgb_color)

# DMC Colors singleton
_dmc_colors = None

def _CreateDMCColors():
  global _dmc_colors  
  csv_data = _GetCsvString()
  lines = csv_data.splitlines()

  # Skip first line
  lines = lines[1:]
  reader = csv.reader(lines, delimiter='\t')

  dmc_colors = set()
  for row in reader:
   dmc_colors.add(_CreateDmcColorFromRow(row))

  return dmc_colors
      
def GetDMCColors():
  global _dmc_colors
  if not _dmc_colors:
    _dmc_colors = frozenset(_CreateDMCColors())
  return _dmc_colors

def GetClosestDMCColorsPairs(rgb_color):
  pairs = list()

  for dcolor in GetDMCColors():
    pairs.append((dcolor, color.RGBColor.distance(rgb_color, dcolor.color)))

  return sorted(pairs, key=lambda pair: pair[1])

def GetClosestDMCColors(rgb_color):
  return [pair[0] for pair in GetClosestDMCColorsPairs(rgb_color)]

class DMCColor(object):
  def __init__(self, number, name, color):
    self.number = number
    self.name = name
    self.color = color

  def __str__(self):
    return super(DMCColor, self).__str__() + str((self.number, self.name, self.color))

def GetStringForDMCColor(dmc_color):
  return "%s %s %s" % (dmc_color.number, dmc_color.name, dmc_color.color)
  
# Simple executable functionality for debugging.
def main():
  for color in GetDMCColors():
    print color

if __name__ == '__main__':
  main()    




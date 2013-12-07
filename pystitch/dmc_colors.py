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
  red, green, blue = color.RGBTupleFromHexString(hex_color)
  return DMCColor(number, name, red, green, blue)

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
  

class DMCColor(color.RGBColor):
  def __init__(self, number, name, red, green, blue):
    self.number = number
    self.name = name
    super(DMCColor, self).__init__(red, green, blue)

# Simple executable functionality for debugging.
def main():
  for color in GetDMCColors():
    print color

if __name__ == '__main__':
  main()    




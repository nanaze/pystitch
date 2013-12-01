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
  print row
  number = int(row[0])
  name = row[1]
  red = int(row[2])
  green = int(row[3])
  blue = int(row[4])
  return DMCColor(number, name, red, green, blue)

class DMCColor(color.RGBColor):
  def __init__(self, number, name, red, green, blue):
    self.number = number
    self.name = name
    super(DMCColor, self).__init__(red, green, blue)

def main():
  csv_data = _GetCsvString()
  lines = csv_data.splitlines()

  # Skip first line
  lines = lines[1:]

  reader = csv.reader(lines, delimiter='\t')

  dmc_colors = list()
  for row in reader:
    dmc_colors.append(_CreateDmcColorFromRow(row))

  print dmc_colors

main()

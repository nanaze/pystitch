"""
Find the closest DMC colors for a hex color.

Usage: python closest_colors.py <hexcolor>
"""

import sys

from .. import color
from .. import dmc_colors


def main():
  if len(sys.argv) < 2:
    sys.exit(__doc__)
  
  hex_color = sys.argv[1]

  rgb_color = color.RGBColorFromHexString(hex_color)

  print 'Given RGB color', rgb_color
  print 
  print 'Closest DMC colors by distance:'
  for pair in dmc_colors.GetClosestDMCColorsPairs(rgb_color):
    print 'Distance:', pair[1], dmc_colors.GetStringForDMCColor(pair[0])

if __name__ == '__main__':
  main()


#!/usr/bin/env python

"""Utilities to generate HTML from an image.

Can be called from commandline. Usage:

gen_html.py image.png
"""

from PIL import Image

import os
import sys
import image, dmc_colors

def PrintPixelArrayTable(pix_arr):

  print "<style> table { border-spacing: 1px; } </style>"

  colors = set()
  width, height = pix_arr.size

  print '<table>'
  for y in xrange(height):
    print '<tr>'
    for x in xrange(width):
      style = 'width: 6px; height: 6px;'
      color = pix_arr[x,y]
      if color:
        style += ' background-color: rgb(%s,%s,%s)' % color
      print '<td style="%s"></td>' % style
    print '</td>'
  print '</table>'

def _GetImage(filename):
  main_dir = os.path.dirname(__file__)
  megaman_path = os.path.join(main_dir, filename)
  img = Image.open(filename).convert('RGBA')
  return img

def main(argv):
  if len(argv) != 2:
    sys.exit(__doc__)

  path = argv[1]
  img = _GetImage(path)
  pix_arr = image.GetPixelArrayFromImage(img)
  PrintPixelArrayTable(pix_arr)

if __name__ == '__main__':
  main(sys.argv)

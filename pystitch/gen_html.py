from PIL import Image

import os

import image, dmc_colors
import megaman

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



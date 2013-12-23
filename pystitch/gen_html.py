#!/usr/bin/env python

"""Utilities to generate HTML from an image.

Can be called from commandline. Usage:

gen_html.py image.png
"""

from PIL import Image

import os
import sys
import image, dmc_colors
import color_map
import color

def _GetTextColor(bg_color):
  average = sum(bg_color) / float(len(bg_color))
  average_float = average / (255 / 2.0)
  if average_float >= 0.5:
    return color.RGBColor(0,0,0)

  return color.RGBColor(255,255,255)

def _GetCssRgbColor(color):
  return 'rgb(%s,%s,%s)' % color

def PrintPixelArrayTable(pix_arr, color_map=None):

  print """
  <style> 
  body {
    font-family: Arial, sans-serif;
  }
  
  table.grid {
    border-spacing: 1px; 
    font-size: 6px;
    font-weight: bold;
  }

  .grid td {
    overflow: hidden;
    width: 6px;
    height: 6px;
  }
  </style>
  """

  colors = set()
  width, height = pix_arr.size

  print '<table class="grid">'
  for y in xrange(height):
    print '<tr>'
    for x in xrange(width):
      style = ''
      color = pix_arr[x,y]
      if color:
        style += ' background-color: %s' % _GetCssRgbColor(color)
      print '<td style="%s">' % style
      
      if color_map:
        text_color = _GetTextColor(color)
        print '<span style="color: %s">' % _GetCssRgbColor(_GetTextColor(color))
        print color_map.get(color)
        print '</span>'
        
      print '</td>' 
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

  cmap = color_map.ColorMap()
  PrintPixelArrayTable(pix_arr, cmap)

if __name__ == '__main__':
  main(sys.argv)

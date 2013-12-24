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
    border-collapse:collapse;
    font-size: 6px;
    font-weight: bold;
  }

  .grid td {
    border:solid 1px #888;
  }

  .grid .square  {
    overflow: hidden;
    width: 6px;
    height: 6px;
    text-align: center;
  }

  .swatch {
    padding: 12px;
    display: inline-block;
  
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
      
      if color and color_map:
        text_color = _GetTextColor(color)
        print '<div class="square" style="color: %s">' % _GetCssRgbColor(_GetTextColor(color))
        print color_map.get(color)
        print '</div>'
        
      print '</td>' 
    print '</td>'
  print '</table>'

def _PrintSwatch(color):
  print '<span class=swatch style="background-color: %s"></span>' % _GetCssRgbColor(color)


def _GetColorMapColorsSortedByName(color_map):
  return sorted(color_map, key=lambda c: color_map.get(c))
  
def PrintColorTable(color_map):
  for color in _GetColorMapColorsSortedByName(color_map):
    key = color_map.get(color)
    print '<h3>Color %s</h3>' % key
    print '<p>'
    print str(color)
    _PrintSwatch(color)
    print '</p>' 
    
    print '<h4>Closest colors:</h4>'

    closest_colors = dmc_colors.GetClosestDMCColorsPairs(color)[:5]
    print '<table border=1>'
    print '<tr>'
    print '<th>Distance</th><th>DMC #</th><th>Name</th><th>Color</th>'
    print '<tr>'
    
    for dmc_color, distance in closest_colors:
      print '<tr>'
      print '<td>%s</td>' % distance
      print '<td>%s</td>' % dmc_color.number
      print '<td>%s</td>' % dmc_color.name
      print '<td>'
      _PrintSwatch(dmc_color.color)
      print str(dmc_color.color)

      print '</td>'
      print '</tr>'
    
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
  PrintColorTable(cmap)

if __name__ == '__main__':
  main(sys.argv)

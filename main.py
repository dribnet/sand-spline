#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

from numpy import pi
# from numpy.random import randint
from numpy.random import random
from numpy import linspace
from numpy import column_stack
from numpy import sin
from numpy import cos
from numpy import ones

TWOPI = 1.90*pi

BACK = [1,1,1,1]
FRONT = [0,0,0,0.05]
LIGHT = [0,0,0,0.05]

# SIZE = 5500
SIZE = 2048

EDGE = 0.15
RAD = 0.5-EDGE
INUM = 2000
NOISE_STP = 0.005


def main():

  from modules.sand import Sand
  from render.render import Animate
  from fn import Fn


  fn = Fn(prefix='./res/', postfix='.png')

  sand = Sand(
      SIZE,
      INUM,
      NOISE_STP,
      fn
      )

  ## radial lines
  # n = 50
  # for i, snum in enumerate(linspace(5,100,n).astype('int')):
  #   a = ones(snum, 'float') * i/n*TWOPI
  #   r = sorted(random(size=(snum, 1))*RAD)
  #   xy = 0.5+column_stack((cos(a), sin(a)))*r
  #   sand.init(xy)

  ## horizontal lines
  # n = 50
  # for i, snum in enumerate(linspace(5,100,n).astype('int')):
  #   x = linspace(EDGE, 1.0-EDGE, snum)
  #   y = ones(snum)*(EDGE + (i/(n-1.0))*2*RAD)
  #   xy = column_stack((x,y))
  #   sand.init(xy)

  ## messy spheres
  n = 35
  spin_scale = 0.05 * pi
  for i, snum in enumerate(linspace(10,150,n).astype('int')):
    a = sorted(i * spin_scale + -0.75 * pi + random(snum)*TWOPI)
    r = ones((snum, 1))*(EDGE + (i/(n-1.0))*(RAD-EDGE))
    xy = -0.2 + (i/100.0) * 0.4 + 0.5+column_stack((cos(a), sin(a)))*r
    sand.init(xy)

  ## tidy spheres
  # n = 50
  # for i, snum in enumerate(linspace(20,80,n).astype('int')):
  #   a = linspace(0,TWOPI, snum)
  #   r = ones((snum, 1))*(EDGE + (i/(n-1.0))*(RAD-EDGE))
  #   xy = 0.5+column_stack((cos(a), sin(a)))*r
  #   sand.init(xy)

  render = Animate(SIZE, BACK, FRONT, sand.wrap)
  render.set_line_width(sand.one)
  render.transparent_pix()
  render.set_front(FRONT)

  render.start()


if __name__ == '__main__':
  main()


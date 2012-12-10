#!/usr/bin/env python
"""
Testing all possible export types 

(c) Laurent Perrinet - INT/CNRS
"""

import MotionClouds as mc

name = 'export'

fx, fy, ft = mc.get_grids(mc.N_X, mc.N_Y, mc.N_frame)
color = mc.envelope_color(fx, fy, ft)

name_ = mc.figpath + name
z = color * mc.envelope_gabor(fx, fy, ft)
for vext in ['.h5', '.mpg', '.zip', '.mat']:
    if mc.anim_exist(name_, vext=vext):
        mc.anim_save(z, name_, display=False, vext=vext)

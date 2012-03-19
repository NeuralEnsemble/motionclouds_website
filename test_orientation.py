#!/usr/bin/env python
"""
Exploring the orientation component of the envelope.

"""

import MotionClouds as mc
import numpy

name = 'grating'

#initialize
fx, fy, ft = mc.get_grids(mc.N_X, mc.N_Y, mc.N_frame)
color = mc.envelope_color(fx, fy, ft)

name_ = mc.figpath + name
z = color * mc.envelope_gabor(fx, fy, ft)
mc.figures(fx, fy, ft, z, name_)

# explore parameters
for sigma_div in [1, 2, 3, 5, 8, 13 ]:
    name_ = mc.figpath + name + '-largeband-B_theta-pi-over-' + str(sigma_div).replace('.', '_')
    z = color * mc.envelope_gabor(fx, fy, ft, B_theta=numpy.pi/sigma_div)
    mc.figures(fx, fy, ft, z, name_)

for div in [1, 2, 4, 3, 5, 8, 13, 20, 30]:
    name_ = mc.figpath + name + '-theta-pi-over-' + str(div).replace('.', '_')
    z = color * mc.envelope_gabor(fx, fy, ft, theta=numpy.pi/div)
    mc.figures(fx, fy, ft, z, name_)

V_X = 1.0
for sigma_div in [1, 2, 3, 5, 8, 13 ]:
    name_ = mc.figpath + name + '-B_theta-pi-over-' + str(sigma_div).replace('.', '_') + '-V_X-' + str(V_X).replace('.', '_')
    z = color * mc.envelope_gabor(fx, fy, ft, V_X=V_X, B_theta=numpy.pi/sigma_div)
    mc.figures(fx, fy, ft, z, name_)

for B_sf in [0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.8]:
    name_ = mc.figpath + name + '-B_sf-' + str(B_sf).replace('.', '_')
    z = color * mc.envelope_gabor(fx, fy, ft, B_sf=B_sf,sf_0=0.3)
    mc.figures(fx, fy, ft, z, name_) # ,vext='.zip'

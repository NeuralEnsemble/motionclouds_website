#!/usr/bin/env python
"""

Testing the role of different parameters in ther speed envelope.

"""

import MotionClouds as mc

name = 'speed'

#initialize
fx, fy, ft = mc.get_grids(mc.N_X, mc.N_Y, mc.N_frame)
color = mc.envelope_color(fx, fy, ft) #

# now selects in preference the plane corresponding to the speed with some thickness
name_ = mc.figpath + name
if mc.anim_exist(name_):
    z = color*mc.envelope_speed(fx, fy, ft)
    mc.figures(z, name_)

# explore parameters
if True:
    for V_X in [-1.0, -0.5, 0.0, 0.1, 0.5, 1.0, 4.0]:
        name_ = mc.figpath + name + '-V_X-' + str(V_X).replace('.', '_')
        if mc.anim_exist(name_):
            z = color * mc.envelope_speed(fx, fy, ft, V_X=V_X)
            mc.figures(z, name_)

    for V_Y in [-1.0, -0.5, 0.5, 1.0, 2.0]:
        name_ = mc.figpath + name + '-V_Y-' + str(V_Y).replace('.', '_')
        if mc.anim_exist(name_):
            z = color * mc.envelope_speed(fx, fy, ft, V_X=0.0, V_Y=V_Y)
            mc.figures(z, name_)

    for B_V in [0.001, 0.01, 0.05, 0.1, 0.5, 1.0, 10.0]:
        name_ = mc.figpath + name + '-B_V-' + str(B_V).replace('.', '_')
        if mc.anim_exist(name_):
            z = color * mc.envelope_speed(fx, fy, ft, B_V=B_V)
            mc.figures(z, name_)

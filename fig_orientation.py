#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demonstration of doing plaids sugin MotionClouds. USed to generate page:

https://invibe.net/LaurentPerrinet/SciBlog/2012-10-02

(c) Laurent Perrinet - INT/CNRS

"""

import numpy as np
import MotionClouds as mc
fx, fy, ft = mc.get_grids(mc.N_X, mc.N_Y, mc.N_frame)

name = 'grating'
vext = '.gif'


# show example
table = """
#acl LaurentPerrinet,LaurentPerrinetGroup:read,write,delete,revert All:
    #format wiki
    -----
    = Recruiting different population ratios in V1 using MotionClouds' orientation components =

    """

    theta, B_theta_low, B_theta_high = np.pi/4., np.pi/32, np.pi/.5
    

    mc1 = mc.envelope_gabor(fx, fy, ft, theta=theta, V_X=np.cos(theta), V_Y=np.sin(theta), B_theta=B_theta_low)
    mc2 = mc.envelope_gabor(fx, fy, ft, theta=theta, V_X=np.cos(theta), V_Y=np.sin(theta), B_theta=B_theta_high)
    name_ = name + '_comp1'
    mc.figures(fx, fy, ft, diag1, name_, vext=vext, seed=12234565)
    table += '||<width="33%">{{attachment:' + name_ + '.png||width=100%}}||<width="33%">{{attachment:' + name_ + '_cube.png||width=100%}}||<width="33%">{{attachment:' + name_ + '.gif||width=100%}}||\n'
    name_ = name + '_comp2'
    mc.figures(fx, fy, ft, diag2, name_, vext=vext, seed=12234565)
    table += '||{{attachment:' + name_ + '.png||width=100%}}||{{attachment:' + name_ + '_cube.png||width=100%}}||{{attachment:' + name_ + '.gif||width=100%}}||\n'
    name_ = name
    mc.figures(fx, fy, ft, diag1 + diag2, name, vext=vext, seed=12234565)
    table += '||{{attachment:' + name_ + '.png||width=100%}}||{{attachment:' + name_ + '_cube.png||width=100%}}||{{attachment:' + name_ + '.gif||width=100%}}||\n'
    table += '|||||| This figure shows how one can create !MotionCloud stimuli that specifically target component and pattern cell. We show in the different lines of this table respectively: Top) one motion cloud component (with a strong selectivity toward the orientation perpendicular to direction) heading in the upper diagonal  Middle) a similar motion cloud component following the lower diagonal Bottom) the addition of both components: perceptually, the horizontal direction is predominant. <<BR>> Columns represent isometric projections of a cube. The left column displays iso-surfaces of the spectral envelope by displaying enclosing volumes at 5 different energy values with respect to the peak amplitude of the Fourier spectrum. The middle column shows an isometric view of the  faces of the movie cube. The first frame of the movie lies on the x-y plane, the x-t plane lies on the top face and motion direction is seen as diagonal lines on this face (vertical motion is similarly see in the y-t face). The third column displays the actual movie as an animation. ||\n'

    table += '\n\n'

    table += '== exploring different component angles ==\n'


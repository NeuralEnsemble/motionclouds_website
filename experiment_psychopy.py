#!/usr/bin/env python
# TODO : rename and describe

import RandomCloud as mc

N_X = 256. # size of image
N_Y = N_X # size of image
N_frame = 128.0 # a full period. in time frames

fx,fy,ft = mc.get_grids(N_X,N_Y,N_frame)
color = mc.envelope_color(fx, fy, ft)
env = color *( mc.envelope_donut(fx,fy,ft, V_X= 1.) + mc.envelope_donut(fx,fy,ft, V_X= -1.))
z = 2*mc.rectif(mc.random_cloud(env),  contrast = .5) -1.

# TODO : make a GUI with two threads
from psychopy import *
import time
win = visual.Window([800,800*9/16],fullscr=True)
for i_frame in range(N_frame):
    #creating a new stimulus every time
    stim = visual.PatchStim(win, tex=z[:,:,i_frame], 
        size=(N_X,N_Y), units='pix',
        interpolate=False)
    stim.draw()
    stim.clearTextures()
    win.flip()

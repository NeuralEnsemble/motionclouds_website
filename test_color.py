#!/usr/bin/env python
"""

Testing different colored noised.

"""

import MotionClouds as mc

name = 'color'
fx, fy, ft = mc.get_grids(mc.N_X, mc.N_Y, mc.N_frame)
z = mc.envelope_color(fx, fy, ft)
if mc.anim_exist(mc.figpath + name): mc.figures(z, mc.figpath + name)

# explore parameters
for alpha in [0.0, 0.5, 1.0, 1.5, 2.0]:
    # resp. white(0), pink(1), red(2) or brownian noise (see http://en.wikipedia.org/wiki/1/f_noise
    name_ = mc.figpath + name + '-alpha-' + str(alpha).replace('.', '_')
    if mc.anim_exist(name_):
        z = mc.envelope_color(fx, fy, ft, alpha)
        mc.figures(z, name_)

for ft_0 in [0.125, 0.25, 0.5, 1., 2., 4.]:# time space scaling
    name_ = mc.figpath + name + '-ft_0-' + str(ft_0).replace('.', '_')
    if mc.anim_exist(name_):
        z = mc.envelope_color(fx, fy, ft, ft_0=ft_0)
        mc.figures(z, name_)

for contrast in [0.1, 0.25, 0.5, 0.75, 1.0, 2.0]:
    name_ = mc.figpath + name + '-contrast-' + str(contrast).replace('.', '_')
    if mc.anim_exist(name_):
        im = mc.rectif(mc.random_cloud(mc.envelope_color(fx, fy, ft)), contrast)
        mc.anim_save(im, name_, display=False)

for contrast in [0.1, 0.25, 0.5, 0.75, 1.0, 2.0]:
    name_ = mc.figpath + name + '-energy_contrast-' + str(contrast).replace('.', '_')
    if mc.anim_exist(name_):
        im = mc.rectif(mc.random_cloud(mc.envelope_color(fx, fy, ft)), contrast, method='energy')
        mc.anim_save(im, name_, display=False)

for seed in [123456 + step for step in range(7)]:
    name_ = mc.figpath + name + '-seed-' + str(seed)
    if mc.anim_exist(name_):
        mc.anim_save(mc.rectif(mc.random_cloud(mc.envelope_color(fx, fy, ft), seed=seed)), name_, display=False)

for size in range(5, 7):
    N_X, N_Y, N_frame = 2**size, 2**size, 2**size
    fx, fy, ft = mc.get_grids(N_X, N_Y, N_frame)
    ft_0 = N_X/float(N_frame)
    name_ = mc.figpath + name + '-size-' + str(size).replace('.', '_')
    if mc.anim_exist(name_):
        z = mc.envelope_color(fx, fy, ft, ft_0=ft_0)
        mc.figures(z, name_)

for size in range(5, 8):
    N_frame = 2**size
    fx, fy, ft = mc.get_grids(mc.N_X, mc.N_Y, N_frame)
    ft_0 = N_X/float(N_frame)
    name_ = mc.figpath + name + '-size_T-' + str(size).replace('.', '_')
    if mc.anim_exist(name_): 
        z = mc.envelope_color(fx, fy, ft, ft_0=ft_0)
        mc.figures(z, name_)

name = 'colorfull'
N = 256 #512
fx, fy, ft = mc.get_grids(N, N, N)
for seed in [123456 + step for step in range(1)]:
    if mc.anim_exist(mc.figpath + name):
        mc.anim_save(mc.rectif(mc.random_cloud(mc.envelope_color(fx, fy, ft), seed=seed)), mc.figpath + name, display=False)
        mc.anim_save(mc.rectif(mc.random_cloud(mc.envelope_color(fx, fy, ft), seed=seed)), mc.figpath + name, display=False, vext='.mat')

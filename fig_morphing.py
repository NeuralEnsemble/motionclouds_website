#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demonstration of going from a natural image to a random cloud by shuffling the phase in FFT space

fig_morphing.py

"""
__revision__ = "$Id: fig_morphing.py,v 0121097cce1f 2011/07/04 16:00:41 perrinet $"

import pylab
import numpy as np
import sys
sys.path.append('..')
import RandomCloud as mc

name = 'results/morphing'
vext = '.mpg'

def randomize_phase(image, B_angle=0., vonmises=False, seed=None):
    Fz = np.fft.fftn(image)
    if B_angle>0.:
        np.random.seed(seed=seed)
        if vonmises:
            Fz *= np.exp(1j * np.random.vonmises(mu=0. , kappa=1./B_angle, size=(N_X, N_Y, N_frame))) # mu = np.pi/2.
        else:
            Fz *= np.exp(1j * B_angle * np.random.randn(N_X, N_Y, N_frame))
            
    z = np.fft.ifftn(Fz).real
    return z

def FTfilter(image, FTfilter):
    from scipy.fftpack import fftn, fftshift, ifftn, ifftshift
    from scipy import real
    FTimage = fftshift(fftn(image)) * FTfilter
    return real(ifftn(ifftshift(FTimage)))
# pre-processing parameters
white_f_0 = .5
white_alpha = 1.4
white_N = 0.01
def whitening_filt(size, temporal=True, f_0=white_f_0, alpha=white_alpha, N=white_N):
    """
    Returns the whitening filter.

    Uses the low_pass filter used by (Olshausen, 98) where
    f_0 = 200 / 512

    parameters from Atick (p.240)
    f_0 = 22 c/deg in primates: the full image is approx 45 deg
    alpha makes the aspect change (1=diamond on the vert and hor, 2 = anisotropic)

    """
    # TODO: make range from -.5 to .5
    fx, fy, ft = np.mgrid[-1:1:1j*size[0], -1:1:1j*size[1], -1:1:1j*size[2]]
    if temporal:
        rho = np.sqrt(fx**2+ fy**2 + ft**2) #TODO : test the effect of whitening parameters? seems to leave a trail... + acausal
    else:
        rho = np.sqrt(fx**2+ fy**2)
    low_pass = np.exp(-(rho/f_0)**alpha)
    K = (N**2 + rho**2)**.5 * low_pass
    return  K

def whitening(image):
    """
    Returns the whitened sequence
    """
    K = whitening_filt(size=image.shape)
    white = FTfilter(image, K)
    # normalizing energy
    #    white /= white.max()# std() # np.sqrt(sum(I**2))
    return white
    
def translate(image, vec):
    """
    Translate image by vec (in pixels)

    """
    u, v = vec

    # first translate by the integer value
    image = np.roll(np.roll(image, np.int(u), axis=0), np.int(v), axis=1)
    u -= np.int(u)
    v -= np.int(v)

    # sub-pixel translation
    from scipy import mgrid
    f_x, f_y = mgrid[-1:1:1j*image.shape[0], -1:1:1j*image.shape[1]]
    trans = np.exp(-1j*np.pi*(u*f_x + v*f_y))
    return FTfilter(image, trans)


def translation(image, X_0=0., Y_0=0., V_X=.5, V_Y=0.0, V_noise=.0, width=2.):

    """

    >> pylab.imshow(concatenate((image[16,:,:],image[16,:,:]), axis = -1))

    """
    # translating the frame line_0
    movie = np.zeros(image.shape)
    V_X_, V_Y_ = V_X * (1+ np.random.randn()*V_noise), V_Y * (1+ np.random.randn()*V_noise)
    for i_frame, t in enumerate(np.linspace(0., 1., N_frame, endpoint=False)):
        V_X_, V_Y_ = V_X_ * (1+ np.random.randn()*V_noise), V_Y_ * (1+ np.random.randn()*V_noise)
        movie[:, :, i_frame] = translate((image[:, :, i_frame]), [(width/2 + X_0+t*V_X_*width + 1)*N_X/2., (width/2 + Y_0+t*V_Y_*width+1)*N_Y/2])
    return movie

# image = np.load('../particles/movie/Muybridge_horse_gallop_animated_2.npy')
#    import sys
#    sys.path.append('../particles/')
#    from experiment_line import generate as line
#    size, size_T = 8, 8
#    N_X, N_Y, N_frame = 2**size, 2**size, 2**size_T
#    image = line(N_X, N_Y, N_frame)
#    image = whitening(image)
#image = pylab.imread('fig_wood.png').mean(axis=2).T
# I use instead a movie:
N_frame, N_first = 32., 530
#image = np.load('/Users/sanz/particles/movie/montypython.npy')[:, ::-1, N_first:(N_first+N_frame)]
image = np.load('montypython.npy')[:, ::-1, N_first:(N_first+N_frame)]
#image = np.load('~/sci/dyva/Motion/particles/movie/montypython.npy')[:, ::-1, N_first:(N_first+N_frame)]
#image -= image.mean()
image /= np.abs(image).max()
(N_X, N_Y, N_frame) = image.shape
movie = translation(image)
(N_X, N_Y, N_frame) = movie.shape
movie = whitening(movie)


fx, fy, ft = mc.get_grids(N_X, N_Y, N_frame)
color = mc.envelope_color(fx, fy, ft) #
z_noise = color*mc.envelope_speed(fx, fy, ft)
movie_noise = mc.rectif(mc.random_cloud(z_noise))

## <<< DEBUG
#movie_ = 1. * randomize_phase(movie, B_angle=1e-1) + .02 * movie_noise
#movie_ -= movie_.mean()
#movie_ /= movie_.max()
##im = mc.rectif()
#z = np.absolute(np.fft.fftshift(np.fft.fftn(movie_)))# .real # **2 # + z_noise#
##        z = z[:,::-1,:]
#z /= z.max()
#mc.visualize(fx, fy, ft, z, name=None, thresholds=[0.99, 0.97, 0.94, .89, .75])#
## DEBUG >>>

for B_angle in [1e-1, 1e0, 1e1]:
    name_ = name + '-B_angle-' + str(B_angle).replace('.', '_')
    movie_ = 1. * randomize_phase(movie, B_angle=B_angle) + .0 * movie_noise
    movie_ -= movie_.mean()
    movie_ /= np.abs(movie_).max()
#    movie_= mc.rectif(movie_)
    
    mc.cube(fx, fy, ft, mc.rectif(movie_), name=name_ + '_cube')
    spectrum = np.absolute(np.fft.fftshift(np.fft.fftn(movie_)))# .real # **2 # + z_noise#
#        img = img[:,::-1,:]
    spectrum /= spectrum.max()
    mc.visualize(fx, fy, ft, spectrum, name=name_)#, thresholds=[0.99, 0.97, 0.94, .89, .75])#)#, thresholds=[0.94, .89, .75, .5, .25])
#        mc.anim_save(img, name_, display=False, vext=vext)
#
## control experiment that shows that using a gaussian gives similar results
#for B_angle in [1e-1, 1e0, 2e0, 3e0, 1e1]:
#    name_ = 'figures/' + name + '-non_vonmises-B_angle-' + str(B_angle).replace('.', '_')
#    if mc.anim_exist(name_):
#        im = mc.rectif(randomize_phase(movie, B_angle=B_angle), contrast=0.85)
#        mc.cube(fx, fy, ft, im, name=name_ + '_cube')
#        mc.anim_save(im, name_, display=False, vext=vext)

##
##OLD:
##    #!/usr/bin/env python
##"""
##Demonstration of going from a natural image to a random cloud by shuffling the phase in FFT space
##
##morphing.py
##
##"""
##__revision__ = "$Id: fig_morphing.py,v 0121097cce1f 2011/07/04 16:00:41 perrinet $"
##
### TODO : merge with fig_morphing ?
##import numpy as np
##
##def randomize_phase(image, B_angle=0., vonmises=False, seed=None):
##    Fz = np.fft.fftn(image)
##    if B_angle>0.:
##        np.random.seed(seed=seed)
##        if vonmises:
##            Fz *= np.exp(1j * np.random.vonmises(mu=0. , kappa=1./B_angle, size=(N_X, N_Y, N_frame))) # mu = np.pi/2.
##        else:
##            Fz *= np.exp(1j * B_angle * np.random.randn(N_X, N_Y, N_frame))
##            
##    z = np.fft.ifftn(Fz).real
##    return z
##
##import RandomCloud as mc
##
##name = 'morphing_line'
##vext = '.mpg'
##
###N_frame, N_first = 64., 564
###image = np.load('../particles/movie/montypython.npy')[:, :, N_first:(N_first+N_frame)]
###image = np.load('../particles/movie/Muybridge_horse_gallop_animated_2.npy')
##if True:
##    import sys
##    sys.path.append('../particles/')
##    from experiment_line import generate as line
##    size, size_T = 6, 6
##    N_X, N_Y, N_frame = 2**size, 2**size, 2**size_T
##    image = line(N_X, N_Y, N_frame)
###    image = whitening(image)
##
##
##(N_X, N_Y, N_frame) = image.shape
##fx, fy, ft = mc.get_grids(N_X, N_Y, N_frame)
##
##name_ = 'figures/' + name
##if mc.anim_exist(name_):
##    im = mc.rectif(image, contrast=0.85)
##    mc.cube(fx, fy, ft, im, name=name_ + '_cube')
##    mc.anim_save(image, name_, display=False, vext=vext)
##
##
##for B_angle in [1e-1, 1e0, 2e0, 3e0, 1e1]:
##    name_ = 'figures/' + name + '-B_angle-' + str(B_angle).replace('.', '_')
##    if mc.anim_exist(name_):
##        im = mc.rectif(randomize_phase(image, B_angle=B_angle, vonmises=True), contrast=0.85)
##        mc.cube(fx, fy, ft, im, name=name_ + '_cube')
##        mc.anim_save(im, name_, display=False, vext=vext)
##
### control experiment that shows that using a gaussian gives similar results
##for B_angle in [1e-1, 1e0, 2e0, 3e0, 1e1]:
##    name_ = 'figures/' + name + '-non_vonmises-B_angle-' + str(B_angle).replace('.', '_')
##    if mc.anim_exist(name_):
##        im = mc.rectif(randomize_phase(image, B_angle=B_angle), contrast=0.85)
##        mc.cube(fx, fy, ft, im, name=name_ + '_cube')
##        mc.anim_save(im, name_, display=False, vext=vext)
##
##
##name = 'morphing_loggabor'
##B = 0.02
##ft_0 = 2. 
##color = mc.envelope_color(fx, fy, ft,ft_0=ft_0)
##image = mc.random_cloud(color *mc.envelope_gabor(fx, fy, ft, sf_0=.1, B_theta=np.pi/10, B_sf=B, B_V=B, V_X=-1., loggabor=True), impulse=True)
##
##
##for B_angle in [1e-1, 1e0, 2e0, 3e0, 1e1]:
##    name_ = 'figures/' + name + '-smooth-B_angle-' + str(B_angle).replace('.', '_')
##    if  mc.anim_exist(name_):
##        im = mc.rectif(randomize_phase(image, B_angle=B_angle), contrast=0.85)
##        mc.anim_save(im, name_, display=False, vext=vext)
##
##image = mc.random_cloud(color *mc.envelope_gabor(fx, fy, ft, theta=0.0,sf_0=0.1, loggabor=True), impulse=True)
##for B_angle in [1e-1, 1e0, 2e0, 3e0, 1e1]:
##    name_ = 'figures/' + name + '-sharp-iso-B_angle-' + str(B_angle).replace('.', '_')
##    if  mc.anim_exist(name_):
##        im = mc.rectif(randomize_phase(image, B_angle=B_angle), contrast=0.85)
##        mc.anim_save(im, name_, display=False, vext=vext)
##
##

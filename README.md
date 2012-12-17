# MotionClouds: Model-based stimulus synthesis of natural-like random textures for the study of motion perception

This scripts implement a framework to generate random texture movies with controlled information content. In particular, these stimuli can be made closer to naturalistic textures compared to usual stimuli such as gratings and random-dot kinetograms. We simplified the definition to parametrically define these "Motion Clouds" around the most prevalent feature axis (mean and bandwith): direction, spatial frequency, orientation.

<img src="http://invibe.net/cgi-bin/index.cgi/SciBlog/2011-07-12?action=AttachFile&do=get&target=MotionPlaid_comp1.gif" width="100%">

This work is supported by the European Union project Number FP7-269921, ``BrainScaleS'' (Brain-inspired multiscale computation in neuromorphic hybrid systems), an EU FET-Proactive FP7 funded research project. The project started on 1 January 2011. It is a collaboration of 18 research groups from 10 European countries.

<img src="https://brainscales.kip.uni-heidelberg.de/images/thumb/e/e2/Public--BrainScalesLogo.svg/100px-Public--BrainScalesLogo.svg.png" width="25%">
<img src="https://brainscales.kip.uni-heidelberg.de/images/thumb/8/88/Public--FET--FETTreeLogo.jpg/70px-Public--FET--FETTreeLogo.jpg" width="25%">
<img src="https://brainscales.kip.uni-heidelberg.de/images/thumb/3/3b/Public--EU-FP7Logo.gif/90px-Public--EU-FP7Logo.gif" width="25%">
<img src="https://brainscales.kip.uni-heidelberg.de/images/thumb/5/5b/Public--EU-Logo.gif/90px-Public--EU-Logo.gif" width="25%">

***
## Code example

Motion Clouds are built using a collection of scripts that provides a simple way of generating complex stimuli suitable for neuroscience and psychophysics experiments. It is meant to be an open-source package  that can be combined with other packages such as PsychoPy or VisionEgg.

All functions are implemented in one main script called `MotionClouds.py` that handles the Fourier cube, the envelope functions as well as the random phase generation and all Fourier related processing. Additionally, all the auxiliary visualization tools to plot the spectra and the movies are included. Specific scripts such as `test_color.py`, `test_speed.py`, `test_radial.py` and `test_orientation.py` explore the role of different parameters for each individual envelope (respectively color, speed, radial frequency, orientation). Our aim is to keep the code as simple as possible in order to be comprehensible and flexible. To sum up, when we build a custom  Motion Cloud there are 3 simple steps to follow:

1. set the MC parameters and construct the Fourier envelope, then visualize it as iso-surfaces: 

```python
import MotionClouds as mc
import numpy as np
# define Fourier domain
fx, fy, ft = mc.get_grids(mc.N_X, mc.N_Y, mc.N_frame) 
# define an envelope
envelope = mc.envelope_gabor(fx, fy, ft, 
    V_X=1., V_Y=0., B_V=.1, 
    sf_0=.15, B_sf=.1, 
    theta=0., B_theta=np.pi/8, alpha=1.) 
# Visualize the Fourier Spectrum
mc.visualize(envelope)  
```
2. perform the IFFT and contrast normalization; visualize the stimulus as a 'cube' visualization of the image sequence, 

```python
movie = mc.random_cloud(envelope)
movie = mc.rectif(movie)
# Visualize the Stimulus
mc.cube(movie, name=name + '_cube') 
```
3. export the stimulus as a movie (.mpeg format available), as separate frames (.bmp and .png formats available) in a compressed zipped folder, or as a Matlab matrix (.mat format). 

```python
mc.anim_save(movie, name, display=False, vext='.mpeg')
```

If some parameters are not given, they are set to default values corresponding to a ''standard'' Motion Cloud. Moreover, the user can easily explore a range of different Motion Clouds simply by setting  an array of values for a determined parameter. Here, for example, we generate 8 MCs with increasing spatial frequency `sf_0` while keeping the other parameters fixed to default values:

```python
for sf_0 in [0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]:
    name_ = 'figures/' + name + '-sf_0-' + str(sf_0).replace('.', '_')
    # function performing plots for a given set of parameters
    mc.figures_MC(fx, fy, ft, name_, sf_0=sf_0) 
```

# MotionClouds: installing and running the python scripts

MotionClouds are parameterized stimuli with controlled motion content and no spatial coherence.  They are precisely tuned in the frequency space.

* A full description can be found in Paula S. Leon, Ivo Vanzetta, Guillaume S. Masson, Laurent U. Perrinet. Motion Clouds: Model-based stimulus synthesis of natural-like random textures for the study of motion perception, URL . Journal of Neurophysiology, 107(11):3217--3226, 2012, see  http://www.ncbi.nlm.nih.gov/pubmed/22423003 or http://jn.physiology.org/content/107/11/3217 .

## installing and running the python scripts
This package consists of:
* ```MotionClouds.py``` : the API with all the math and display routines,
* ```test_*.py``` : different types of stimuli are tested,
* ```experiment_*py``` : different experiments.
* ```fig_*py``` : different scripts used to generate wiki pages.
* ```figures``` : resulting figures of tests and experiments (as set in the variable ``MotionClouds.figpath```.
* ```Makefile``` : a GNUmake file to edit files ```make edit```, generate figures ```make figures``` or compile the documentation ```make doc```.

## Installation

* Installation of MotionClouds consists simply in downloading the ```MotionClouds.py``` file which contains all routines to compute and use the MotionClouds textures. This script uses [[http://python.org|python]]] which comes (pre-installed /  easy to download and install) on many operating systems.

* Installation has some dependencies: 
1. mandatory: ```numpy``` is the core library used to compute textures,
1. optional: ```mayavi``` is used to visualize envelopes,
1. optional: ```ffmpeg``` is used to generate movies.
1. optional: ```matplotlib```, ```scipy``` (with PIL support) and ```imagemagick``` are used to generate figures in the documentation.
1. optional: ```progressbar``` for displaying progress of encoding.
1. optional: ```texlive-latex-recommended  latexmk latexdiff``` to compile the documentation 

## download

* to get the latest version, download the current state from the repository:
```
git clone https://github.com/meduz/MotionClouds.git 
```

* other sources exist to get a stable release, such as [[http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=146953|ModelDb]].

### installation using custom scripts 

* depending on your system you should use in a terminal window ```
sh install_dependencies_debian.sh
``` or ```
sh install_dependencies_macosx.sh
```
* an alternative is to use a virtual machine such as for instance the one provided by the [[http://neuro.debian.net/vm.html|NeuroDebian team]].

### Installation in Debian-based distributions (such as Ubuntu)

* Use the ```aptitude``` front end to install packages: (or alternatively ```apt -get``` if you feel confident with that tool instead)

* ```python``` is supported by most distribution and should already be installed. You can check which version is installed : ```
python -V
```

* The same libraries as for MacOsX need to be installed : ```
sudo aptitude install python-scipy python-numpy python-matplotlib
```

* Idem for the progress bar module ```
sudo easy_install progressbar 
```

* Install the ```ffmpeg``` encoder to work with mpeg, avi, etc, videos: ```
sudo aptitude install ffmpeg
```

* Install !LaTeX to compile the documentation: ```
sudo aptitude install texlive-latex-recommended latexmk latexdiff
```

* when creating MoiMoin pages, it is useful to package images in a zip file: ```
aptitude install zip
```

### Installation on MacOsX: EPD

* Enthought distributes a battery-included installation of python. It is recommended to use the i386 version as the 64-bits version lacks a proper compilation of MayaVi. You will still need ```ffmpeg``` to make movies (see HomeBrew or MacPorts section below).

* Similarly, to compile the documentation, I recommend to install !TexLive from the !MacTex distribution available @ https://www.tug.org/mactex/

### Installation on MacOsX: HomeBrew (for more experienced users)

* install it following their https://github.com/mxcl/homebrew/wiki/Installation|instructions : 
```
ruby -e "$(curl -fsSL https://raw.github.com/gist/323731)"
```

* then install the following packages: 

```
# install python through HomeBrew as a framework
brew install python --framework

# bootstrap pip
/usr/local/share/python/easy_install pip
/usr/local/share/python/pip install --upgrade distribute

# libraries
brew install gfortran
pip install -U ipython

# useful packages
pip install -U nose
pip install -U progressbar
easy_install pyreport
easy_install -f http://dist.plone.org/thirdparty/ -U PIL==1.1.7

# numpy et al
pip install -U numpy
pip install -U scipy
pip install -U -e git+git@github.com:matplotlib/matplotlib.git#egg=matplotlib
# pip install -f http://downloads.sourceforge.net/project/matplotlib/matplotlib/matplotlib-1.0/matplotlib-1.0.0.tar.gz matplotlib

# IDE
pip install -U sphinx pyflakes rope
brew install sip
brew install pyqt
pip install -U spyder

# mayavi
brew install vtk --python
pip install -U traitsbackendqt
pip install -U configobj
pip install  -U "Mayavi[app]"
```
* be sure to install ffmpeg : ```
brew install ffmpeg
brew install zip
```

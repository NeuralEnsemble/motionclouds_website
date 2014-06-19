# MotionClouds: installing and running the python scripts

MotionClouds are parameterized stimuli with controlled motion content and no spatial coherence.  They are precisely tuned in the frequency space.

* A full description can be found in Paula S. Leon, Ivo Vanzetta, Guillaume S. Masson, Laurent U. Perrinet. Motion Clouds: Model-based stimulus synthesis of natural-like random textures for the study of motion perception, URL . Journal of Neurophysiology, 107(11):3217--3226, 2012, see  http://www.ncbi.nlm.nih.gov/pubmed/22423003 or http://jn.physiology.org/content/107/11/3217 .

## installing and running the python scripts
This package consists of:
* ```MotionClouds.py``` : the API with all the math and display routines,
* ```test_*.py``` : different types of stimuli are tested,
* ```experiment_*py``` : different experiments.
* ```fig_*py``` : different scripts used to generate wiki pages.
* ```figures``` : resulting figures of tests and experiments (as set in the variable ```MotionClouds.figpath```.
* ```Makefile``` : a GNUmake file to edit files ```make edit```, generate figures ```make figures``` or compile the documentation ```make doc```.

## Installation

*   MotionClouds consist of a one-file python script: Installation consists simply in downloading the ```MotionClouds.py``` file which contains all routines to compute and use the MotionClouds textures. This script uses python (http://python.org) which comes (pre-installed /  easy to download and install) on many operating systems.

* MotionClouds may easily be installed using

```
    pip install MotionClouds
```

* Other solutions consist to simply grab this file at: https://raw.githubusercontent.com/NeuralEnsemble/MotionClouds/master/MotionClouds.py and to use it along with the examples.

* Installation has some dependencies:
 1. mandatory: ```numpy``` is the core library used to compute textures,
 1. optional: ```mayavi``` is used to visualize envelopes,
 1. optional: ```ffmpeg``` is used to generate movies.
 1. optional: ```matplotlib```, ```scipy``` (with PIL support) and ```imagemagick``` are used to generate figures in the documentation.
 1. optional: ```progressbar``` for displaying progress of encoding.
 1. optional: ```texlive-latex-recommended  latexmk latexdiff``` to compile the documentation
 1. optional: ```PyOpenGL PyOpenGL_accelerate glumpy``` to display MotionClouds online

## download

* to get the latest version, download the current state from the repository:
```
git clone https://github.com/meduz/MotionClouds.git
```

* other sources exist to get a stable release, such as ModelDb (http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=146953).

### installation using custom scripts

* depending on your system you should use in a terminal window ```
sh install_dependencies_debian.sh
``` or ```
sh install_dependencies_macosx.sh
```
* an alternative is to use a virtual machine such as for instance the one provided by the NeuroDebian team (http://neuro.debian.net/vm.html).

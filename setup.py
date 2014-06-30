#!/usr/bin/env python

from distutils.core import setup

setup(
    name = "MotionClouds",
    version = "0.1.1",
    packages = ['MotionClouds'],
    package_dir = {'MotionClouds': ''},
    author = "Laurent Perrinet INT - CNRS",
    author_email = "Laurent.Perrinet@univ-amu.fr",
    description = "Model-based stimulus synthesis of natural-like random textures for the study of motion perception.",
#     long_description=open("README.md").read(),
    license = "GPLv2",
    keywords = ('computational neuroscience', 'simulation', 'analysis', 'visualization', 'parameters'),
    url = 'https://github.com/NeuralEnsemble/MotionClouds', # use the URL to the github repo
    download_url = 'https://github.com/NeuralEnsemble/MotionClouds/tarball/0.1',
    classifiers = ['Development Status :: 3 - Alpha',
                   'Environment :: Console',
                   'License :: OSI Approved :: GNU General Public License (GPL)',
                   'Operating System :: POSIX',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Utilities',
                  ],
     )

#!/bin/bash

# 1. install Xcode:
# From this url : (uncomment the following line)
# open http://itunes.apple.com/us/app/xcode/id497799835?mt=12
# install Xcode on the Mac App Store by clicking on “View in Mac App Store”.

# 2. install HomeBrew
ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
# to reinstall, do:
# rm -rf /usr/local/Cellar /usr/local/.git && brew cleanup

# Make sure we’re using the latest Homebrew
brew update

# Upgrade any already-installed formulae
brew upgrade

# install python through HomeBrew

pip install --upgrade setuptools
pip install --upgrade distribute

# bootstrap pip
pip install --upgrade setuptools
pip install --upgrade distribute

# numpy et al
brew install gcc
brew install cmake
brew install fftw
brew install libtool
brew install hdf5
brew tap homebrew/science
brew tap Homebrew/python
pip install -U numexpr
pip install -U cython
pip install -U tables
pip install -U pandas
brew install numpy #--with-openblas
brew test numpy

# pylab
brew install matplotlib --with-tex

# mayavi
brew install vtk5 --with-qt
#brew install vtk --python
#pip install traitsbackendqt
pip install configobj
pip install envisage
pip install  "Mayavi[app]"
# HDF export
brew install hdf5
pip install cython
pip install numexpr
pip install tables

brew install wxpython
pip install -U psychopy
pip install pyprind


# install online displaying tools
pip install PyOpenGL PyOpenGL_accelerate
pip install glumpy
brew install --HEAD smpeg
brew install pygame
pip install hg+https://pyglet.googlecode.com/hg/
pip install -U NeuroTools

# convert
brew install imagemagick
brew install x264
brew install ffmpeg

# Remove outdated versions from the cellar
brew cleanup

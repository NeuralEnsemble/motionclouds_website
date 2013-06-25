# install XCode
# From this url : http://itunes.apple.com/us/app/xcode/id497799835?mt=12 install Xcode on the Mac App Store by clicking on “View in Mac App Store”.

# install HomeBrew
ruby -e "$(curl -fsSkL raw.github.com/mxcl/homebrew/go)"
# to reinstall, do:
# rm -rf /usr/local/Cellar /usr/local/.git && brew cleanup

brew update
brew upgrade

# an alternative is to install EPD:
# sudo rm -fr /Library/Frameworks/EPD64.framework /Applications/Enthought 
# sudo remove-EPD-7.2-2
# hdiutil attach /Volumes/tera_enigma/data/soft/epd-7.2-2-macosx-x86_64.dmg
# hdiutil attach /Volumes/tera_enigma/data/soft/epd-7.2-2-macosx-i386.dmg
# sudo installer -pkg /Volumes/EPD-7.2/EPD.mpkg -target /
# hdiutil detach  /Volumes/EPD-7.2

#echo ---- bashrc -----
#cat ~/.bashrc
#echo ----------------

#echo -----login------
#cat ~/.login
#echo ----------------

#echo ---- bashrc -----
#cat ~/.bash_profile
#echo ----------------

#echo ". ~/.bashrc" >> ~/.bash_profile
#echo "export ENV=$HOME/.bashrc" >> ~/.bash_profile
#echo "export PATH=/usr/local/share/python:/usr/local/Cellar/python/2.7.3/Frameworks/Python.framework/Versions/2.7/bin:/usr/local/bin:/usr/local/sbin:/Users/lup/.gem/ruby/1.8/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/X11/bin " >> ~/.bash_profile
#echo "export PYTHONPATH=/usr/local/Cellar/python/2.7.3/Frameworks/Python.framework/Versions/Current/lib/python2.7/site-packages/">> ~/.bash_profile
#source  ~/.bash_profile # also calls bashrc
#echo $PATH
#echo $PYTHONPATH
#source ~/.bash_profile

# install python through HomeBrew as a framework
brew install readline sqlite gdbm pkg-config
brew install python

# bootstrap pip
/usr/local/share/python/easy_install pip
pip install --upgrade distribute
# pip install ipython
brew install pyside pyside-tools
pip install sphinx
pip install spyder

# numpy et al
brew install gfortran
brew install cmake
brew install fftw
brew install umfpack
brew install libtool
brew install ffmpeg
pip install numpy
pip install PIL
pip install scipy
pip install git+git://github.com/matplotlib/matplotlib.git
# mayavi
brew install --pyqt --python --qt vtk
#brew install vtk --python
#pip install traitsbackendqt
pip install configobj
pip install envisage
pip install  --user "Mayavi[app]"
# HDF export
brew install hdf5 
pip install cython
pip install numexpr
pip install tables

# install online displaying tools
pip install PyOpenGL PyOpenGL_accelerate
pip install glumpy

# convert
brew install imagemagick

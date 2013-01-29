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

# cd /System/Library/Frameworks/Python.framework/Versions
# sudo rm Current
# ln -s /usr/local/Cellar/python/2.7.3/Frameworks/Python.framework/Versions/Current

# install python through HomeBrew as a framework
brew install readline sqlite gdbm pkg-config
brew install python

# bootstrap pip
/usr/local/share/python/easy_install pip
pip install --upgrade distribute
# pip install -U ipython
# brew remove qt
# cd `brew --prefix`
# brew versions qt
# git checkout 83f742e Library/Formula/qt.rb
# brew install qt
# brew install pyqt
brew install pyside pyside-tools
pip install --user sphinx
pip install --user spyder

# numpy et al
brew install gfortran
brew install libtool libagg¬
brew install ffmpeg
pip install --user numpy
pip install --user PIL
pip install --user scipy
# brew install libtool libagg
# pip install --user matplotlib
pip install git+git://github.com/matplotlib/matplotlib.git
# mayavi
brew install vtk --python
pip install --user traitsbackendqt
pip install --user configobj
pip install  --user "Mayavi[app]"
# HDF export
brew install hdf5 
pip install --user cython
pip install --user numexpr
pip install --user tables

# convert
brew install imagemagick

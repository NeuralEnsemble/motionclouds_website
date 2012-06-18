# install HomeBrew
/usr/bin/ruby -e "$(/usr/bin/curl -fsSL https://raw.github.com/mxcl/homebrew/master/Library/Contributions/install_homebrew.rb)"

brew update
brew upgrade

# install EPD
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
brew install python --framework --universal
mkdir -p ~/Library/Frameworks/Python.framework/Versions
ln -s "/usr/local/Cellar/python/2.7.3/Frameworks/Python.framework/Versions/2.7" ~/Library/Frameworks/Python.framework/Versions/2.7
ln -s ~/Library/Frameworks/Python.framework/Versions/2.7 ~/Library/Frameworks/Python.framework/Versions/Current
ln -s ~/Library/Frameworks/Python.framework/Versions/2.7/Python ~/Library/Frameworks/Python.framework/Python
ln -s ~/Library/Frameworks/Python.framework/Versions/2.7/Resources ~/Library/Frameworks/Python.framework/Resources

# bootstrap pip
/usr/local/share/python/easy_install pip
pip install --user distribute
pip install --user ipython
brew install qt
# brew install pyqt
brew install pyside	pyside-tools
pip install --user sphinx
pip install --user spyder

# numpy et al
brew install --user  gfortran
brew install --user ffmpeg
pip install --user numpy
pip install --user PIL
pip install --user scipy
# brew install libtool libagg
# pip install --user matplotlib
pip install git+git://github.com/matplotlib/matplotlib.git
#pip install -U -e git+git@github.com:matplotlib/matplotlib.git#egg=matplotlib
# mayavi
brew install vtk --python
pip install -U --user traitsbackendqt
pip install --user configobj
pip install  --user "Mayavi[app]"
# HDF export
brew install --user hdf5 
pip install --user cython 
pip install --user numexpr 
pip install --user tables 

# convert
brew install imagemagick

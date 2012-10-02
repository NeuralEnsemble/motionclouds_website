# install HomeBrew
# /usr/bin/ruby -e "$(curl -fsSL https://raw.github.com/gist/323731)"

brew update
brew upgrade

# install EPD
# sudo rm -fr /Library/Frameworks/EPD64.framework /Applications/Enthought 
# sudo remove-EPD-7.2-2
# hdiutil attach /Volumes/tera_enigma/data/soft/epd-7.2-2-macosx-x86_64.dmg
hdiutil attach /Volumes/tera_enigma/data/soft/epd-7.2-2-macosx-i386.dmg
sudo installer -pkg /Volumes/EPD-7.2/EPD.mpkg -target /
hdiutil detach  /Volumes/EPD-7.2

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
source ~/.bash_profile

# cd /System/Library/Frameworks/Python.framework/Versions
# sudo rm Current
# ln -s /usr/local/Cellar/python/2.7.3/Frameworks/Python.framework/Versions/Current

# install python through HomeBrew as a framework
brew install readline sqlite gdbm pkg-config
rm -fr ~/Frameworks 
brew install python --framework --universal
mkdir ~/Frameworks
ln -s "/usr/local/Cellar/python/2.7.3/Frameworks/Python.framework" ~/Frameworks

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
# brew install pyside	pyside-tools
# pip install sphinx
# pip install spyder

# numpy et al
brew install gfortran
brew install ffmpeg 
pip install -U numpy
pip install -U PIL
pip install -U scipy
#pip install -U -e git+git@github.com:matplotlib/matplotlib.git#egg=matplotlib
pip install -U matplotlib
#brew install libtool libagg
#pip install git+git://github.com/matplotlib/matplotlib.git


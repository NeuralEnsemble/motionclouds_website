# installing dependencies on Debian for MotionClouds
# --------------------------------------------------
sudo apt-get install aptitude
# it is always a good idea to update/upgrade your system before
sudo aptitude update
sudo aptitude upgrade

# A script for the impatient:
# uncomment to fit your installation preference
# others should read the README.txt doc.

#
# 1) minimal install 
#
# sudo aptitude install python-numpy python-scipy 

#
# 2) minimal install with visualization and generation of documentation
#
# sudo aptitude install python-numpy python-scipy mayavi2 python-matplotlib ffmpeg
# sudo aptitude install texlive-latex-recommended  latexmk latexdiff

#
# 3) full install with python editor and libraries for various export types
#
sudo aptitude install libavcodec-extra-53 python-gmpy python-numpy python-scipy mayavi2 python-matplotlib ffmpeg spyder liblzo2-2 python-tables imagemagick texlive-latex-recommended latexmk latexdiff zip ipython-notebook psychopy

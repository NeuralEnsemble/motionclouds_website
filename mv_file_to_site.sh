#! /bin/sh

numero=0

if test $# = $numero
	then echo "file to move in arg"
	exit
fi
mkdir site_dir
mv $* site_dir
mv site_dir ~/
git checkout site
mv ~/site_dir ./new_add

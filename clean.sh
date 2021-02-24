#!/bin/sh
nikola clean
rm -rf output
rm .doit.db
rm -rf posts/.ipynb_checkpoints
rm *.pyc
rm -rf results
rm -rf posts/results

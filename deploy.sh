#!/bin/sh
lftp -c "
open invibe@ftp.invibe.net;
mirror --reverse --delete -vvv ./output /motionclouds
"

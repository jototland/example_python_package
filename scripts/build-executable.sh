#! /bin/sh

# This is a Bourne shell script.
# If you have git-bash, busybox, Cygwin, WSL, etc, you can run this in Windows as well.
#
# This is a simple wrapper to build mainprogram.exe from mainprogram.py
# (the only complication is that PATHSEP is : on unix and ; on dos/windows)
#
# To include non-python-files with pyinstaller, use `--add-files` on the
# command line to pyinstaller


PATHSEP=:
uname | grep -iq windows && PATHSEP=';'
pyinstaller -F --add-data "mypackage${PATHSEP}mypackage" mainprogram.py

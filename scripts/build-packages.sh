#! /bin/sh

# This is a Bourne shell script.
# If you have git-bash, busybox, Cygwin, WSL, etc, you can run this in Windows as well.
# (this script is so simple that it will work even in powershell or cmd.exe if you rename it)
#
# This is the command line to build both a sdist and bdist at the same time.
#
# In order for bdist_wheel to work:
# pip install wheel

python setup.py sdist bdist_wheel


#! /bin/sh

# This is a Bourne shell script.
# If you have git-bash, busybox, Cygwin, WSL, etc, you can run this in Windows as well.
#
# It simply deletes some files that either python, setup.py or pyinstaller creates

find . -name __pycache__ | xargs rm -rf build dist *.egg-info *.spec .pytest_cache

# This is __main.py__ inside the Python package mypackage
#
# This naming convention makes it possible to run this file from the command
# line as:
#   `python -m mypackage`
#
# This file should not be imported by other modules

from . import hello

def main():
    hello()

if __name__ == '__main__':
    main()

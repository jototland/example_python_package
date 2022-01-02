# This is an example program outside mypackage.
# When mypackage is installed, you can run it as `python mainprogram.py`

from mypackage.hello import hello

def main():
    hello()

if __name__ == '__main__':
    main()

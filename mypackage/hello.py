# This is hello.py
#
# It contains a single function, which prints a greeting, twice.
#
# Instead of hardcoding the greetings, they are read (using
# `importlib.resources`) from text files contained inside this package.
#
# I demonstrate two methods of doing this below. Only the bottom method will
# work with files contained in a subdirectory of the package.
#
# Note: storing data inside a package is only something you should consider if
# the data is never changed by the program or library. So do not do this with
# databases, etc...

import importlib.resources as r


def hello():
    with r.open_text('mypackage', 'hello.txt', encoding='utf-8') as f:
        msg = f.read().strip()
    print(msg)

    msg = (r.files('mypackage') / 'subdir/hello.txt').read_text(encoding='utf-8').strip()
    print (msg)

# Example python package

This is an example python package, written for my own use. It is not meant as a
general recommendation (and I'm not an expert in python packaging).

The goal of this package is to help *me* remember what needs to go into
`setup.py`, `MANIFEST.in`, etc, and how I can construct python packages, or
standalone executables from python source code.

Please also read: pkgdata-info.md

Notes:

It seems setup.py is now outdated, and you should use `setup.cfg` and
`pyproject.toml` instead of, or in addition to `setup.py`. However, as of this
moment, I can't see any reason to change. Python packaging seems to be a moving
target, and putting everything in `setup.py`. still works just fine. Until the
maintainers have made up their mind, it surely seems easier to edit just
`setup.py` than to guess what goes into the two new ones.

When developing a package, use `pip install -e .` inside you venv, that will
install the package as a development package. By doing this, your tests (which
usually live in a different directory) can still find your package.


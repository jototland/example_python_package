# How to include *data* in python packaging distributions

## Introduction

There are two relevant package distribution formats:
 - `sdist`
 - `wheel`

`sdist` is a source distribution. If it's not all python, it will typically
contain C source code in addition to python code.

`wheel` is a binary distribution. If it's not all python, it will typically
contain platform dependent shared libraries.

If your package contains non-python data-files, such as templates, test-data,
image-files, etc, then neither package format will include them by default.

`wheel`s can only contain data that is inside a package directory.

You can create these distributions (assuming you've created a suitable
`setup.py`) using the single combined command:
    `python setup.py sdist bdist_wheel`

## Files controlling data files to include:

There are two files that determine which data files go into which distributions:

## `setup.py`

The variables of interest is:
- `include_package_data` : bool
- `package_data` : a dictionary where:
    - the keys are package names
    - the values are lists of files
- `exclude_package_data` : dict<br>
  (similar to `package_data`)

With these variables, it is only possible to include data from package
directories.

## `MANIFEST.in`

The allowable commands are:
- include glob1 glob2 ...
- exclude glob1 glob2 ...
- recursive-include dirglob glob1 glob2 ...
- recursive-exclude dirglob glob1 glob2 ...
- global-include glob1 glob2 ...
- global-exclude glob1 glob2 ...
- graft dirglob
- prune dirglob

It is possible to specify data from any directory, not just packaging
directories.

## A recommendation

It's recommended to include everything, and exclude the things you don't need.
This is better than missing a file, and having the package not work.

## `sdist`:

A file is included in an `sdist` if either:
- It is included (and not excluded) by `MANIFEST.in`
- The file is on of:
    - `setup[.py|.cfg]`
    - `README[|.txt|.md|.rst]`
    - `pyproject.toml`
    - `MANIFEST.in`
    - `license_file` in `setup.py` lists it
- `include_package_data=False` and both:
    - `package_data` lists the file
    - `exclude_package_data` does not list the file

## `wheel`:

A file is included in a `wheel` if all of the following is true:
- the file is inside a package directory
- `exclude_package_data` does not list the file
- either:
    - `package_data` lists the file
    - `include_package_data=True` and the file is included (and not excluded) by `MANIFEST.in`.

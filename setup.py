# This is an example setup.py
# The comments give further explanation.

from pathlib import Path
import setuptools


# read package names from `requirements.in`.
def pkgs_from_requirements_in():
    with open('requirements.in', 'rt', encoding='utf-8') as f:
        return [
            word for word in
            (line.partition('#')[0].strip() for line in f)
            if word != ''
        ]

# recursive globs in `package_data` are broken
def recursive_glob(pkg, *globs):
    path = pkg.replace('.', '/')
    rmv = path + '/'
    root = Path(path)
    return [f.as_posix().replace(rmv, '')
            for g in globs
            for f in root.glob(g)]

def subdir_list(path):
    return [rdf[0] for rdf in os.walk(path)]


# This is where the magic happens...
setuptools.setup(

    # there are only 4 required fields:
    name='mypackage',
    version='0.0.0',
    description='',
    packages=setuptools.find_packages(
        exclude=[
            'tests'
        ],
    ),
    # or more explicitly: packages=['mypackage'],

    # If your python packages are in one or more subdirectories, say it here:
    # (This is a mapping from package to directory, the mapping from empty
    # string is a default)
    package_dir={
        "": '.',
        "otherpackage": "src",
    },

    # Only python .py-files are by default included in a bdist package.
    # See pkgdata-info.md for more details...
    include_package_data=True,
    package_data={'mypackage': recursive_glob('mypackage', '**/*.bin')},
    exclude_package_data={ "mypackage": ["donotincludeinbdist.txt", ], },

    # How to automatically create an entry in venv/bin (or venv/scripts)
    entry_points={
        "console_scripts": ["hello=mypackage.hello:hello"],
    },

    python_requires='>=3.5',

    install_requires=pkgs_from_requirements_in(),
    # or more explicitly: install_requires=['flask', 'requests', 'pytest',],

    # Optionally set zip_safe to either True or False
    # If you don't set it manually, setuptools will analyze and guess
    # Are you unsure: set to False
    zip_safe=True,

    # less important optional fields and metadata

    url = 'https://github.com/jototland/mypackage',
    author = 'Jo Totland',
    author_email = 'jototland@gmail.com',

    license="WTFPL",
    license_file="LICENSE.txt",

    long_description_content_type="text/markdown",
    long_description="""
A *very* long description
""",

    # https://pypi.org/classifiers/
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating Systen :: OS Independent",
        "Topic :: Software Development :: Documentation",
        "License :: Public Domain",
        "Natural Language :: Norwegian",
    ],
)

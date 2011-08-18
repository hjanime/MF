import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "MfPy",
    version = "0.1",
    author = "Marinka Zitnik",
    author_email = "marinka@zitnik.si", 
    description = "Python Matrix Factorization Techniques for Data Mining",
    url = "http://orange.biolab.si/trac/wiki/MatrixFactorization",
    packages = ["mfpy"],
    packages_dir = { "mfpy": "./mfpy"},
    license = "OSI Approved :: GNU General Public License (GPL)",
    long_description = read("README.rst"),
    classifiers = [
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering"
    ]
    )
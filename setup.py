# -*- coding: utf-8 -*-
#
# Author: Charles B Drotar <drotarcharles@gmail.com>
#
# Setup the accessiplot module. 

import os
from distutils.core import setup
from setuptools import find_packages

def do_setup():
    # Minimum allowed version
    MIN_PYTHON = (3, 8)

    # get the installation requirements:
    with open('requirements.txt') as req:
        REQUIREMENTS = [l for l in req.read().split(os.linesep) if l]
        print(f"Requirements: {REQUIREMENTS}")

    setup(name='accessiplot',
        version='0.0.1',
        description='Accessiblity accessor for Matplotlib plots',
        author='Charles B Drotar',
        author_email='drotarcharles@gmail.com',
        url='https://github.com/charlesdrotar/accessiplot',
        classifiers=[
            'Intended Audience :: Science/Research',
            'Intended Audience :: Education',
            'License :: OSI Approved :: Python Software Foundation License',
            'Topic :: Scientific/Engineering',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX',
            'Operating System :: Unix',
            'Operating System :: MacOS',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Topic :: Scientific/Engineering :: Visualization'
        ],
        python_requires=f'>={MIN_PYTHON[0]}.{MIN_PYTHON[1]}',
        install_requires=REQUIREMENTS,
        # Adapted from: https://github.com/inmanta/inmanta/pull/83
        # See also: https://github.com/pypa/setuptools/issues/3197
        packages=find_packages(),
        keywords='accessibility visualization matplotlib'
    )


if __name__ == '__main__':
    do_setup()
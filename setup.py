#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
https://github.com/kennethreitz/setup.py
Note: To use the 'upload' functionality of this file, you must:
  $ pip install twine
"""
from __future__ import print_function
import io
import sys
from os import path, system
from shutil import rmtree

# Always prefer setuptools over distutils
from setuptools import find_packages, setup, Command

here = path.abspath(path.dirname(__file__))

# Import the README.rst and use it as the long-description.
with io.open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()


class PublishCommand(Command):
    """Support setup.py publish."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        system('twine upload dist/*')

        sys.exit()


# This is where the magic happens:
setup(
    name='PizzaPy',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.0.1',

    description='A Python Program to Pizza.',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/roshancode/PizzaPy',

    author='Roshan Lamichhhane',
    author_email='roshanlamichhanenepali@gmail.com',
    keywords='Order Pizza',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4',
        # 'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'pyhamcrest',
        'requests', 
        'xmltodict',
    ],
    include_package_data=True,
    tests_require=[
        'mock',
        'pytest',
    ],
    cmdclass={
        'publish': PublishCommand,
    },
)

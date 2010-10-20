#!/usr/bin/env python

from distutils.core import setup

setup(name='boomslang',
        version='0.4b',
        description='A thin layer over matplotlib that simplifies creation of common plots',
        author='Alex C. Rasmussen',
        author_email='alexras@acm.org',
        url='http://code.google.com/p/boomslang/',
        packages=['boomslang'],
        package_dir={'boomslang':''},
        license='BSD')

# vim: set ts=4 sw=4 expandtab:

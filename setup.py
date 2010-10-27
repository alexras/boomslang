#!/usr/bin/env python

from distutils.core import setup

setup(name='boomslang',
        version='0.4b',
        description='A thin layer over matplotlib that simplifies creation of common plots',
        author='Alex C. Rasmussen',
        author_email='alexras@acm.org',
        url='http://code.google.com/p/boomslang/downloads/detail?name=boomslang-0.4b.tar.gz&can=2&q=',
        classifiers = [f.strip() for f in """
                     Development Status :: 4 - Beta
                     Intended Audience :: Developers
                     License :: OSI Approved :: BSD License
                     Natural Language :: English
                     Operating System :: OS Independent
                     Programming Language :: Python 2
                     Topic :: Software Development :: Libraries :: Python Modules
                     """.splitlines() if f.strip()],
        license='BSD',
        requires = ['matplotlib'],
        packages=['boomslang'],
        package_dir={'boomslang':''})

# vim: set ts=4 sw=4 expandtab:

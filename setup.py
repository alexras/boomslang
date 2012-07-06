#!/usr/bin/env python

from distutils.core import setup

setup(name='boomslang',
      version='1.0',
      download_url='http://boomslang.googlecode.com/files/boomslang-0.6b.tar.gz',
      description='A thin layer over matplotlib that simplifies creation of common plots',
      long_description='''I created Boomslang to decrease the amount of boilerplate
code I had to write when producing graphs for research papers. Boomslang
treats data and plots separately and encapsulates them both in objects,
giving the programmer the ability to author modular, re-usable graphing
code.''',
      author='Alex Rasmussen',
      author_email='alexras@acm.org',
      url='http://code.google.com/p/boomslang/',
      keywords=['matplotlib'],
      classifiers = [f.strip() for f in """
                     Development Status :: 4 - Beta
                     Environment :: Other Environment
                     Intended Audience :: Developers
                     License :: OSI Approved :: BSD License
                     Natural Language :: English
                     Operating System :: OS Independent
                     Programming Language :: Python
                     Programming Language :: Python :: 2.7
                     Topic :: Software Development :: Libraries :: Python Modules
                     """.splitlines() if f.strip()],
      license='BSD',
      requires = ['matplotlib'],
      packages=['boomslang'],
      package_dir={'boomslang':''})

# vim: set ts=4 sw=4 expandtab:

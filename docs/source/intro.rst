Introduction
============

I created Boomslang to decrease the amount of boilerplate code I had to write
when producing plots for research papers. Boomslang treats both plots and plot
data as objects. This allows functions to return plot data or plots, and allows
plots to be flexibly and cleanly composed. Boomslang also abstracts away much
of Matplotlib's syntax, which can be confusing and brittle if not used
properly.

Prerequisites
-------------

Boomslang requires a recent version of `matplotlib`_.

Installation
------------

As a Python Egg (via pip or easy_install)
-----------------------------------------

The latest stable version of Boomslang is available from `easy_install`_ or
`pip`_.

.. code-block:: python

    easy_install boomslang
    pip install boomslang

This will install Boomslang in your Python installation's site-packages
directory.

Installing the development version
----------------------------------

If you want the latest features, it's probably best to use the development
version of Boomslang until it reaches a point where I bring it out of beta. To
do this, install `git`_ and clone the repository:

.. code-block:: python

   git clone git://github.com/alexras/boomslang.git

Once you've cloned Boomslang, you can either add it to your `PYTHONPATH` or
symlink it to your site-packages directory.

.. _git: http://git-scm.org/
.. _pip: http://pypi.python.org/pypi/pip
.. _easy_install: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _matplotlib: http://matplotlib.github.com/

#!/usr/bin/env python

import subprocess
import os
import shlex

with open("plot_elements.rst", "w+") as fp:
    # Get a list of all classes that subclass
    subproc = subprocess.Popen(
        'grep -lE "class .*?\(PlotInfo\)" ../*.py', stdout=subprocess.PIPE,
        stderr=None, shell=True)

    (stdout, stderr) = subproc.communicate()

    print >>fp, """
Plot Elements
=============


.. autoclass:: boomslang.PlotInfo.PlotInfo
    :members:
    :undoc-members:
"""

    for line in stdout.split():
        line = os.path.basename(line.strip())

        if line[:2] == "__":
            continue

        class_name = line[:-3]

        print >>fp, """
%(class_name)s
%(underline)s
.. autoclass:: boomslang.%(class_name)s.%(class_name)s
    :members:
    :inherited-members:
    :undoc-members:""" % {
            "class_name" : class_name,
            "underline" : '-' * len(class_name)
            }


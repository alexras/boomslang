#!/usr/bin/env python

import os, sys, glob

IMAGE_PREFIX = ".. image:: "

examples = {}

# Read the script corresponding to each example into memory
for image in glob.glob("examples/*.png"):
    script_file = os.path.splitext(image)[0] + ".py"

    if not os.path.exists(script_file):
        sys.exit("Can't find script for %s" % (image))

    with open(script_file, 'r') as fp:
        examples[image] = fp.readlines()

# Determine the maximum number of columns used by a script's source and image
# path

max_image_path_cols = None
max_script_cols = None

for image, script in examples.items():
    max_script_cols = max(max(map(lambda x: len(x) + 5, script)),
                          max_script_cols)
    max_image_path_cols = max(len(image) + len(IMAGE_PREFIX),
                              max_image_path_cols)

# Construct table where the first column is an example image and the second
# column is the source code that generates that image

fp = open("examples.rst", 'w+')
#fp = sys.stdout

print >>fp,"""
Examples
========

.. htmlonly::
"""

print >>fp, '+%s+%s+' % ('-' * (max_image_path_cols + 2),
                         '-' * (max_script_cols + 2))

print >>fp, '|%s|%s|' % ("Image".ljust(max_image_path_cols + 2),
                         "Source Code".ljust(max_script_cols + 2))

print >>fp, '+%s+%s+' % ('=' * (max_image_path_cols + 2),
                         '=' * (max_script_cols + 2))

for image, script in examples.items():
    print >>fp, "|%s|%s|" % (
        (IMAGE_PREFIX + image).ljust(max_image_path_cols + 2),
        ("::").ljust(max_script_cols + 2))

    print >>fp, "|%s|%s|" % (
        "    :width: 100 %".ljust(max_image_path_cols + 2),
        "".ljust(max_script_cols + 2))

    for line in script:
        print >>fp, "|%s|%s|" % ("".ljust(max_image_path_cols + 2),
                                 ("    " + line.strip()).ljust(
                max_script_cols + 2))

    print >>fp, '+%s+%s+' % ('-' * (max_image_path_cols + 2),
                             '-' * (max_script_cols + 2))


fp.close()

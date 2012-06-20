#!/usr/bin/env python

import os, sys, glob
from PIL import Image

IMAGE_PREFIX = ".. image:: "

examples = []

# Find all example images and their corresponding scripts
for image in glob.glob("examples/*.png"):
    script_file = os.path.splitext(image)[0] + ".py"

    if not os.path.exists(script_file):
        sys.exit("Can't find script for %s" % (image))

    example_name = os.path.basename(script_file)[:-3]

    image_file = Image.open(image)
    (width, height) = image_file.size

    examples.append((example_name,
        {"image" : image,
         "script" : script_file,
         "width" : width,
         "height" : height
         }))

examples.sort(key = lambda x: x[1]["width"])

# Make a page of image links that link images to individual code examples
with open("examples.rst", 'w+') as fp:
    print >>fp,"""

.. _examples-gallery:

Examples
========

This page provides a gallery of example Boomslang scripts. Clicking on one of
the images below will direct you to that image and a listing of its source code.

    """

    for (example_name, example_info) in examples:
        print >>fp, """
.. image:: %s
   :target: examples-%s.html
    """ % (example_info["image"], example_name)

# Create a page for each image that shows the image and its source code

for (example_name, example_info) in examples:
    with open("examples-%s.rst" % (example_name), "w+") as fp:
        header = "Examples: %s" % (example_info["script"])
        print >>fp, header
        print >>fp, "=" * len(header)

        print >>fp, """

.. image:: %s

Back to :ref:`examples-gallery`

.. code-block:: python
    :linenos:

""" % (example_info["image"])

        with open(example_info["script"]) as script_fp:
            leading_space_skip = True

            for line in script_fp:
                line = line.strip()

                print >>fp, "    %s" % (line)

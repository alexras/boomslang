import matplotlib
import math
import collections
import re
import sys
from Line import Line
from Bar import Bar

def getGoldenRatioDimensions(width):
    goldenRatio = (math.sqrt(5) - 1.0) / 2.0
    return (width, goldenRatio * width)

def getXYValsFromFile(filename, regex, postFunction=None,
                      autofillXValues=False):
    fp = open(filename)

    regex = re.compile(regex)

    matches = []

    i = 0
    for line in fp:
        line = line.strip()

        match = regex.match(line)

        if match is not None:
            matchGroups = match.groups()

            if postFunction is not None:
                matchGroups = postFunction(matchGroups)
            else:
                matchGroups = [float(x) for x in matchGroups]

            if len(matchGroups) < 2 or autofillXValues:
                matchGroups.insert(0, i)

            matches.append(matchGroups)
            i += 1
    fp.close()

    matches.sort()

    xValues = []
    yValues = []

    for matchGroups in matches:

        numMatchGroups = len(matchGroups)

        if len(yValues) == 0:
            yValues = [[] for i in xrange(numMatchGroups - 1)]

        xValues.append(matchGroups[0])
        for i in xrange(1, numMatchGroups):
            yValues[i-1].append(matchGroups[i])


    return [xValues, yValues]

def getLinesFromFile(filename, regex, postFunction=None, autofillXValues=False):
    """
    Turn a regularly-structured file into a collection of
    :class:`boomslang.Line.Line` objects.

    Parses each line in `filename` using the regular expression `regex`. By
    default, the first matching group from the regular expression gives the
    x-axis value for a set of points and all subsequent matching groups give
    the y-axis values for each line. If `postFunction` is not None, it is a
    function that is applied to the matching groups before they are inserted
    into the lines. If `autofillXValues` is True, all matching groups are
    treated as y-axis values for lines and the x-axis value is the line number,
    indexed from 0.

    Returns a list of :class:`boomslang.Line.Line` objects.

    **Example:** Suppose I had a file `blah.txt` that looked like this::

       1980 - 1, 2, 3
       1981 - 4, 5, 6
       1982 - 7, 8, 9

    The snippet below shows the result of running :py:func:`boomslang.Utils.getLinesFromFile` on `blah.txt`:

       >>> lines = boomslang.Utils.getLinesFromFile("blah.txt", "(\d+) - (\d+), (\d+), (\d+)")
       >>> len(lines)
       3
       >>> lines[0].xValues
       [1980, 1981, 1982]
       >>> lines[1].xValues
       [1980, 1981, 1982]
       >>> lines[2].xValues
       [1980, 1981, 1982]
       >>> lines[0].yValues
       [1, 4, 7]
       >>> lines[1].yValues
       [2, 5, 8]
       >>> lines[1].yValues
       [3, 6, 9]

    """

    (xValues, yValues) = getXYValsFromFile(filename, regex, postFunction,
                                           autofillXValues)

    lines = []

    for i in xrange(len(yValues)):
        line = Line()
        line.xValues = xValues[:]
        line.yValues = yValues[i][:]
        lines.append(line)
    return lines

def getBarsFromFile(filename, regex, postFunction=None, autofillXValues=False):
    """
    Turns a regularly-structured file into a collection of
    :class:`boomslang.Bar.Bar` objects.

    For more details on arguments, see :py:func:`getLinesFromFile`.

    Returns a list of :class:`boomslang.Bar.Bar` objects.
    """

    (xValues, yValues) = getXYValsFromFile(filename, regex, postFunction,
                                           autofillXValues)

    bars = []

    for i in xrange(len(yValues)):
        bar = Bar()
        bar.xValues = xValues[:]
        bar.yValues = yValues[i][:]
        bars.append(bar)
    return bars

def cdf(values):
    """
    Returns a :class:`boomslang.Line.Line` representing the CDF of the list of
    values given in `values`.
    """

    line = Line()
    cdfValues = values[:]
    cdfValues.sort()

    count = float(len(cdfValues))

    line.xValues = cdfValues
    line.yValues = [float(x) / count for x in xrange(1, int(count) + 1)]
    assert(count == len(line.yValues))

    return line

def getCDF(values):
    return cdf(values)

def histogram(values, binSize):
    """
    Returns a :class:`boomslang.Line.Line` representing a histogram of the list
    of values given in `values` with bin size `binSize`.
    """

    line = Line()
    line.stepFunction('post')

    bins = collections.defaultdict(int)

    maxBin = 0

    for value in values:
        currentBin = value / binSize
        bins[currentBin] += 1
        maxBin = max(maxBin, currentBin)

    for currentBin, binCount in bins.items():
        nextBin = currentBin + binSize

        if nextBin not in bins:
            bins[nextBin] = 0

    for currentBin in sorted(bins.keys()):
        line.xValues.append(currentBin * binSize)
        line.yValues.append(bins[currentBin])

    return line

def _check_min_matplotlib_version(*min_version_pieces):
    def version_piece_to_int(piece):
        if piece == 'x':
            return 0
        else:
            return int(piece)

    version_pieces = [version_piece_to_int(x)
                      for x in matplotlib.__version__.split('.')]

    return _check_min_version(version_pieces, min_version_pieces)

def _check_min_version(version_pieces, min_version_pieces):
    for i, min_version_piece in enumerate(min_version_pieces):
        version_piece = version_pieces[i]

        if (version_piece > min_version_piece or
            (i == len(min_version_pieces) - 1 and
             version_piece >= min_version_piece)):
            return True
        elif version_piece < min_version_piece:
            return False

    return False


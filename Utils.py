import matplotlib
import math
import re
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
    (xValues, yValues) = getXYValsFromFile(filename, regex, postFunction,
                                           autofillXValues)

    bars = []

    for i in xrange(len(yValues)):
        bar = Bar()
        bar.xValues = xValues[:]
        bar.yValues = yValues[i][:]
        bars.append(bar)
    return bars

def getCDF(values):
    line = Line()
    cdfValues = values[:]
    cdfValues.sort()

    count = float(len(cdfValues))

    line.xValues = cdfValues
    line.yValues = [float(x) / count for x in xrange(1, int(count) + 1)]
    assert(count == len(line.yValues))

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


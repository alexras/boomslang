import math
import re
from Line import Line
from Bar import Bar

def getGoldenRatioDimensions(width):
    goldenRatio = (math.sqrt(5) - 1.0) / 2.0
    return (width, goldenRatio * width)

def getXYValsFromFile(filename, regex, postFunction=None):
    fp = open(filename)
    
    regex = re.compile(regex)
    
    matches = []
    
    for line in fp:
        line = line.strip()
        
        match = regex.match(line)
        
        if match is not None:
            matchGroups = match.groups()
            
            if len(matchGroups) < 2:
                print >>sys.stderr, "Need at least two matching groups to construct a line"
                sys.exit(1)
            
            if postFunction is not None:
                matchGroups = postFunction(matchGroups)
            else:
                matchGroups = [float(x) for x in matchGroups]
            matches.append(matchGroups)
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

def getLinesFromFile(filename, regex, postFunction=None):
    (xValues, yValues) = getXYValsFromFile(filename, regex, postFunction)
    
    lines = []
    
    for i in xrange(len(yValues)):
        line = Line()
        line.xValues = xValues[:]
        line.yValues = yValues[i][:]
        lines.append(line)
    return lines
    
def getBarsFromFile(filename, regex, postFunction=None):
    (xValues, yValues) = getXYValsFromFile(filename, regex, postFunction)
    
    bars = []
    
    for i in xrange(len(yValues)):
        bar = Bar()
        bar.xValues = xValues[:]
        bar.yValues = yValues[i][:]
        bars.append(bar)
    return bars
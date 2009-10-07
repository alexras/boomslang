import math

def getGoldenRatioDimensions(width):
    goldenRatio = (math.sqrt(5) - 1.0) / 2.0
    return (width, goldenRatio * width)

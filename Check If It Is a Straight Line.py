# Given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
# Checks if these points make a straight line in the XY plane.


def checkStraightLine(coordinates):
    if(len(coordinates) == 2):
        return True
    if((coordinates[1][0] - coordinates[0][0]) == 0):
        for x, y in coordinates:
            if(x != coordinates[1][0]):
                return False
        return True
    m = (coordinates[1][1] - coordinates[0][1]) / \
        (coordinates[1][0] - coordinates[0][0])
    n = (coordinates[0][1]) - (m*(coordinates[0][0]))
    for x, y in coordinates:
        if((m*x+n) != y):
            return False
    return True

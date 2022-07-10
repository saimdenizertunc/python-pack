# Given two integers, x and y, which represent current location on a Cartesian grid: (x, y).
# Also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi).
# A point is valid if it shares the same x-coordinate or the same y-coordinate.
# Return the index(0-indexed) of the valid point with the smallest Manhattan distance from current location.
# If there are multiple, return the valid point with the smallest index.
# If there are no valid points, return -1.
# The Manhattan distance between two points(x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).

def nearestValidPoint(x, y, points):
    def manDis(first: list, second: list) -> int:
        return (abs(first[0]-second[0]) + abs(first[1]-second[1]))
    result = []
    for idx, val in enumerate(points):
        if(val[0] == x and val[1] == y):
            return idx
        if(val[0] == x or val[1] == y):
            result.append([manDis([x, y], val), idx])
        if (len(result) == 0):
            return -1

    return sorted(result)[0][1]

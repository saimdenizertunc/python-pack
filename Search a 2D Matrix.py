# Algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties
# - Integers in each row are sorted from left to right.
# - The first integer of each row is greater than the last integer of the previous row.


def searchMatrix(matrix, target):
    if(matrix[-1][-1] < target or matrix[0][0] > target):
        return False
    else:
        for i in matrix:
            if (i[0] > target or i[-1] < target):
                continue
            else:
                for x in i:
                    if (x == target):
                        return True
                return False

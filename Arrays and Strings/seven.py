#
# 1.7
#
# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0

def insert_zeroes(matrix):
    elements_to_change = set([])
    M = len(matrix) # columns
    N = len(matrix[0]) # rows; assume at least 1x1 matrix
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if element == 0:
                elements_to_change.add((i, j))
    print elements_to_change

    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[i])):
            if (i, j) in elements_to_change:
                matrix[i] = [0 for k in xrange(N)] # change column
                for x in xrange(M):
                    matrix[x][j] = 0

matrix = [[0, 3, 5], [4, 6, 2]]
insert_zeroes(matrix)
print matrix

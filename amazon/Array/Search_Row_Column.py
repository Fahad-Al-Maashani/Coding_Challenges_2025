"""
Given a matrix mat[][] and an integer x, the task is to check if x is present in mat[][] or not. Every row and column of the matrix is sorted in increasing order.

Examples: 

Input: x = 62, mat[][] = [[3, 30, 38],
                                        [20, 52, 54],
                                        [35, 60, 69]]
Output: false
Explanation: 62 is not present in the matrix.


Input: x = 55, mat[][] = [[18, 21, 27],
                                          [38, 55, 67]]
Output: true
Explanation: mat[1][1] is equal to 55.


Input: x = 35, mat[][] = [[3, 30, 38],
                                        [20, 52, 54],
                                        [35, 60, 69]]
Output: true
Explanation: mat[2][0] is equal to 35.
"""
# Python program to search an element in row-wise
# and column-wise sorted matrix

def matSearch(mat, x):
    n = len(mat)
    m = len(mat[0])
  
    for i in range(n):
        for j in range(m):
            if mat[i][j] == x:
                return True
  
    # If x was not found, return false
    return False

if __name__ == "__main__":
    mat = [[3, 30, 38],
           [20, 52, 54],
           [35, 60, 69]]
    x = 35
    if matSearch(mat, x):
        print("true")
    else:
        print("false")


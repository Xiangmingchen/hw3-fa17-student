import math
##################################
#                                #
#  Homework 3                    #
#  Released: September 26, 2017  #
#  Due: October 10, 2017         #
#                                #
##################################


# Matrix Transpose
#
# Description:
#     Given an m x n matrix A, return A^T, that is,
#     return the transpose of the matrix A.
#
# Example(s):
#
#     Example 1:
#         Input:
#             A = [[1]]
#         Output:
#             [[1]]
#
#     Example 2:
#         Input:
#             A = [[1, 2, 3],
#                  [4, 5, 6],
#                  [7, 8, 9]]
#         Output:
#             [[1, 4, 7],
#              [2, 5, 8],
#              [3, 6, 9]]
#
def matrix_transpose(A):
    B = []
    for i in range(len(A[0])):
        B.append([None] * len(A))

    for i in range (len(A)):
        for j in range (len(A[0])):
            B[j][i] = A[i][j]

    return B



# Max Element in 2-D Array
#
# Description:
#     Given a 2-d array grid of integers,
#     determine the maximum number in grid.
#
# Example(s):
#     Example 1:
#         Input:
#             grid = [[4, 2],
#                     [3, -1]]
#         Output:
#             4
#
#     Example 2:
#         Input:
#             grid = [[-300, -200],
#                     [-300, -100]]
#         Output:
#             -100
#
def max_2d_array(grid):
    max = grid[0][0]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > max:
                max = grid[i][j]
    return max




# Binary Search
#
# Description:
#     Given a sorted (increasing) array with distinct integers and a
#     target integer, determine the index of target in the given array.
#     If target is not in the array, return None. Try to use the fact
#     that the array is sorted to optimize your algorithm.
#
# Example(s):
#
#     Example 1:
#         Input:
#             arr = [1, 2, 3, 4, 5]
#             target = 3
#         Output:
#             2
#
#     Example 2:
#         Input:
#             arr = [1, 2, 3, 4, 5]
#             target = 0
#         Output:
#             None
#
def binary_search(arr, target):
    # A easy way to do it
    # try:
    #     return arr.index(target)
    # except:
    #     return None

    # now let's try the hard way
    index = len(arr) // 2
    def bSearch(arr, target, index): #index = len(arr) // 2

        i = len(arr) // 2
        #if target is in the middle, return the middle index
        if target == arr[i]:
            return index
        #if reaching the end of the list, return None
        elif len(arr) == 1:
            return None
        #else if target is smaller than the middle, binary_search the left half
        elif target < arr[i]:
            arr = arr[:i]
            index = index - len(arr) // 2 - 1
            return bSearch(arr, target, index)
        #else if the target is larger than the middle, binary_search the right half
        elif target > arr[i]:
            arr = arr[i + 1:]
            index = index + len(arr) // 2 + 1
            return bSearch(arr, target, index)

    return bSearch(arr, target, index)



# Sorted Matrix Search
#
# Description:
#     Given a square 2d array of integers and a target integer
#     return the coordinates of the target integer as a tuple
#     in the form (row, col) if the element exists in the matrix,
#     or None if the element does not exists. The 2d array
#     is guaranteed to be sorted ascending row-wise,
#     and the zeroth element of each row is strictly larger than
#     the last element of the previous row.
#
# Example(s):
#     Example 1:
#         Input:
#             arr = [[1 , 2 ,  3],
#                    [8 , 11, 16],
#                    [23, 24, 25]]
#             target = 8
#         Output:
#             (1, 0)
#
#     Example 2:
#         Input:
#             arr = [[1 , 2 ,  3],
#                    [8 , 11, 16],
#                    [23, 24, 25]]
#             target = 20
#         Output:
#             None
#
def search_2d_array(arr, target):
    flattened = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            flattened.append(arr[i][j])
    try:
        index = flattened.index(target)
    except:
        return None
    else:
        row = math.ceil((index + 1) / len(arr)) - 1
        col = index % len(arr)
        return [row, col]



# Maximum Sum Subarray
#
# Description:
#     Given an array of integers, determine the maximum sum of
#     a continuous subarray of the given array.
#
# Examples(s):
#     Example 1:
#         Input:
#             arr = [1, 2, 3, 4, 5]
#         Ouput:
#             15
#
#     Example 2:
#         Input:
#             arr = [1, -3, 4, 1, -2, 3]
#         Output:
#             6
#
def max_sum_subarray(arr):
    max = arr[0]
    for i in range(len(arr)):
        for j in range(len(arr) - i):
            sum = 0
            for k in range(i + 1):
                sum += arr[j + k]
            if sum > max:
                max = sum

    return max



# Maximum Sum Sub-Rectangle
#
# Description:
#     Given a 2-d array of integers, determine the
#     maximum sub-rectangle sum.
#
# Example(s):
#     Example 1:
#         Input:
#             grid = [[1, 2],
#                     [3, 4]]
#         Output:
#             10
#
#     Example 2:
#         Input:
#             grid = [[1,  2],
#                     [-3, 0]]
#         Ouput:
#             3
#
#     Example 3:
#         Input:
#             grid = [[ 1, -2,  0],
#                     [-1,  3,  0],
#                     [ 3, -1, -9]]
#         Output:
#             4
#
def max_sum_subrectangle(arr):
    max = arr[0][0]
    for i in range(len(arr)):
        for j in range(len(arr) - i):
            for m in range(len(arr[0])):
                for n in range(len(arr[0]) - m):
                    sum = 0
                    for k in range(i + 1):
                        for l in range(m + 1):
                            sum += arr[j + k][n + l]
                    if sum > max:
                        max = sum

    return max



# Maximum Number of Times an Array can be Flattened
#
# Description:
#     Given an array of integers and arrays,
#     return the maximum number of times arr can be flattened.
#     For example, if arr = [1, 2, [3, 4], 5],
#     then arr could be flattened once.
#
# Example(s):
#     Example 1:
#         Input:
#             arr = [1, 2, [3, 4], 5]
#         Output:
#             1
#
#     Example 2:
#         Input:
#             arr = [1, 2, 3, 4, 5]
#         Output:
#             0
#
def max_array_flatten(arr):
    stringA = str(arr)
    count = 0
    max = 0
    for char in stringA:
        if char == '[':
            count += 1
        elif char == ']':
            count -= 1
        if count > max:
            max = count
    return max - 1

# https://leetcode.com/problems/search-a-2d-matrix/
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    n = len(matrix)
    m = len(matrix[0])
    left = 0
    right = n - 1
    while left < right:
        mid = math.ceil((left + right) / 2)
        if matrix[mid][0] <= target:
            left = mid
        else:
            right = mid - 1
    i = left
    left = 0 
    right = m - 1
    while left < right:
        mid = (left + right) >> 1
        if matrix[i][mid] < target:
            left = mid + 1
        else:
            right = mid
    return True if matrix[i][left] == target else False
class Solution(object):
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        columns = len(matrix[0])

        left = 0
        right = rows * columns - 1

        while left <= right:
            mid = (left + right) // 2
            mid_value = matrix[mid // columns][mid % columns]
            if mid_value > target:
                right = mid - 1
            elif mid_value < target:
                left = mid + 1
            else:
                return True

        return False

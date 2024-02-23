class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        n, m = len(matrix), len(matrix[0])
        low, high = 0, n * m - 1

        while low <= high:
            mid = (low + high) // 2
            mid_x, mid_y = mid // m, mid % m

            if matrix[mid_x][mid_y] == target:
                return True
            elif matrix[mid_x][mid_y] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False            

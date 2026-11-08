class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        for row in matrix:
            if target < row[0]:
                return False
            elif target >= row[0] and target <= row[-1]:
                break
            elif row == matrix[-1] and target > row[-1]:
                return False

        l, r = 0, len(row) -1
        while l <= r:
            m = (l + r) // 2
            if target > row[m]:
                l = m+1
            elif target < row[m]:
                r = m-1
            else:
                return True
        return False

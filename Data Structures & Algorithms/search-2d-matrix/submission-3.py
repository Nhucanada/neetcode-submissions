class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        t, b = 0, len(matrix) - 1

        while t <= b:
            n = (t + b) // 2

            if target > matrix[n][-1]:
                t = n + 1
            elif target < matrix[n][0]:
                b = n - 1
            else:
                break
        else:
            return False

        l, r = 0, len(matrix[n]) -1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[n][m]:
                l = m+1
            elif target < matrix[n][m]:
                r = m-1
            else:
                return True
        return False

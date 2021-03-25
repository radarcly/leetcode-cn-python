from typing import List
# 方法一 标记数组
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = [0] * len(matrix)
        cols = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows[i] = 1
                    cols[j] = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0
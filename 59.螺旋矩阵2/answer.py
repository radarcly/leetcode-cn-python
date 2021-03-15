from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ret = [[0] * n for _ in range(n)]
        i, j = 0, n - 1
        num = 1
        while i < j:
            for k in range(i, j + 1):
                ret[i][k] = num
                num += 1
            for k in range(i + 1, j):
                ret[k][j] = num
                num += 1
            for k in range(j, i - 1, -1):
                ret[j][k] = num
                num += 1
            for k in range(j - 1, i, -1):
                ret[k][i] = num
                num += 1
            i, j = i + 1, j - 1            
        if i == j:
            ret[i][j] = num
        return ret
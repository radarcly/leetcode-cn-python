from typing import List
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        n = len(A)
        for i in range(n):
            left, right = 0, n - 1
            while left < right:
                #由于是翻转 再反转 所以如果两者不同的话就是其本身不用考虑
                if A[i][left] == A[i][right]:
                    A[i][left] ^= 1 # 异或
                    A[i][right] ^= 1
                left += 1
                right -= 1
            if left == right:
                A[i][left] ^= 1
        return A


from bisect import bisect
A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
K = 2
class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        length = len(A)
        P = [0]
        for num in A:
            P.append(P[-1] + (1 - num))  # P数组为前缀和数组
        ans = 0
        for right in range(length):
            left = bisect.bisect_left(P, P[right + 1] - K)
            ans = max(ans, right - left + 1)
        return ans
solution = Solution()
print(solution.longestOnes(A, K))
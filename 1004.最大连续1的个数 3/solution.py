from bisect import bisect
class Solution:
    def longestOnes(self, A, K):
        n = len(A)
        P = [0]
        for num in A:
            P.append(P[-1] + (1 - num)) # P数组为前缀和数组，长度是A数组+1，第一项为0
        ans = 0
        for right in range(n):
            # bisect 为 python 二分查找库
            # bisect(haystack,needle)在haystack（干草垛）里搜索 needle（针）的位置，
            # 该位置满足的条件是，把 needle 插入这个位置之后， haystack 还能保持升序。
            # 也就是在说这个函数返回的位置前面的值，都小于或等于 needle 的值。
            left = bisect.bisect_left(P, P[right + 1] - K)
            # bisect_left函数是新元素会被放置于它相等的元素的前面，而 bisect_right返回的则是跟它相等的元素之后的位置。
            ans = max(ans, right - left + 1)
        return ans



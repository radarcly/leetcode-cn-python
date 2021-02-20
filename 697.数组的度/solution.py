# 官方题解 哈希表
class Solution:
    def findShortestSubArray(self, nums):
        mp = dict()
        for i, num in enumerate(nums):
            if num in mp:
                mp[num][0] += 1
                mp[num][2] = i
            else:
                mp[num] = [1, i, i]
        maxNum = minLen = 0
        for count, left, right in mp.values():
            if maxNum < count:
                maxNum = count
                minLen = right - left + 1
            elif maxNum == count:
                if minLen >  right - left + 1:
                    minLen = right - left + 1
        return minLen


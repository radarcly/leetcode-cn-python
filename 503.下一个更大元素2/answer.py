class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        n = len(nums)
        for i in range(n):
            for j in range(1,n):
                index = (i + j) % n
                if nums[index] > nums[i]:
                    ret.append(nums[index])
                    break
            if len(ret) != i + 1:
                ret.append(-1)
        return ret
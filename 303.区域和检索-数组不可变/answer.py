class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        sum = 0
        for k in range(i,j+1):
            sum += self.nums[k]
        return sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
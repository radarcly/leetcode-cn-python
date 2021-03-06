from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [-1] * n
        stk = list()  # stk即为单调栈 存的是ind
        # 每次我们移动到数组中的一个新的位置i，我们就将当前单调栈中所有对应值小于nums[i]的下标弹出单调栈，
        # 这些值的下一个更大元素即为nums[i]

        for i in range(n * 2 - 1):
            while stk and nums[stk[-1]] < nums[i % n]:
                ret[stk.pop()] = nums[i % n]
            stk.append(i % n)

        return ret

#示例 nums=[1,2,1,3,2,1]
#遍历元素 循环次数 栈中元素(实际存的为下标) 返回值
#1       1        1                     [-1,-1,-1,-1,-1,-1]
#2       2        2                     [ 2,-1,-1,-1,-1,-1]
#1       3        2 1                   [ 2,-1,-1,-1,-1,-1]
#3       4        3                     [ 2, 3, 3,-1,-1,-1]
#2       5        3 2                   [ 2, 3, 3,-1,-1,-1]
#1       6        3 2 1                 [ 2, 3, 3,-1,-1,-1]
#1       7        3 2 1                 [ 2, 3, 3,-1,-1,-1]
#2       8        3 2                   [ 2, 3, 3,-1,-1, 2]
#1       9        3 2                   [ 2, 3, 3,-1,-1, 2]
#3       10       3                     [ 2, 3, 3,-1, 3, 2]
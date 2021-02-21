from collections import deque

from sortedcontainers import SortedList
class Solution:
    # 方法一 滑动窗口 + 有序集合
    def longestSubarray(self, nums, limit) -> int:
        s = SortedList()
        n = len(nums)
        left = right = ret = 0

        while right < n:
            s.add(nums[right])
            # 一旦有序列表中最大值 - 最小值 大于limit 就从有序列表中删掉nums中最左边的元素，直到最大值-最小值小于limit
            while s[-1] - s[0] > limit:
                # remove函数按value删除，重复元素只会删除一次
                s.remove(nums[left])
                left += 1
            ret = max(ret, right - left + 1)
            right += 1
        return ret

    # 方法二 滑动窗口 + 单调队列
    class Solution:
        def longestSubarray2(self, nums, limit) -> int:
            n = len(nums)
            queMax, queMin = deque(), deque()
            left = right = ret = 0

            while right < n:
                # 如果新元素比最大队列数大，就删除最大数列前面所有比它大的数 最大数列单调递减，保证最大队列队首是当前最大值
                while queMax and queMax[-1] < nums[right]:
                    queMax.pop()
                # 如果新元素比最小队列数小，就删除最小数列前面所有比它小的数 最小数列单调递增，保证最小队列队首是当前最小值
                while queMin and queMin[-1] > nums[right]:
                    queMin.pop()

                # 加入最新的数
                queMax.append(nums[right])
                queMin.append(nums[right])

                # 如果最大值减最小值大于limit，left+1 最小队列 or 最大队列 如果含有此数也进行删除
                while queMax and queMin and queMax[0] - queMin[0] > limit:
                    if nums[left] == queMin[0]:
                        queMin.popleft()
                    if nums[left] == queMax[0]:
                        queMax.popleft()
                    left += 1

                ret = max(ret, right - left + 1)
                right += 1

            return ret








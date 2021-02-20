class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 构造长度为50000的数组
        l = [0] * 50000
        for num in nums:
            l[num] += 1 # 统计num数组中每个元素出现次数
        m = 0
        elements = []
        # 以下for循环找出出现次数最多的 num 储存在 elements 数组中，最多次数存储在m中
        for index, value in enumerate(l):
            if value > m:
                m = value
                elements = [index]
            elif value == m:
                elements.append(index)
        result = 50000
        if m > 1:
            # 每次循环找出对应element 出现的起始位置和结束位置进行相减
            for element in elements:
                count = 1
                begin = 0
                end = 0
                for i,j in enumerate(nums):
                    if j == element and count == 1:
                        begin = i
                        count += 1
                    elif j == element and count == m:
                        end = i
                    elif j == element:
                        count += 1
                # 找出起始位置和结束位置最近的element
                if result > end - begin + 1:
                    result = end - begin + 1
            return result
        else:
            return 1

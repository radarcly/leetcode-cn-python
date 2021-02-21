import bisect
nums = [7,40,10,10,40,39,96,21,54,73,33,17,2,72,5,76,28,73,59,22,100,91,80,66,5,49,26,45,13,27,74,87,56,76,25,64,14,86,50,38,65,64,3,42,79,52,37,3,21,26,42,73,18,44,55,28,35,87]
limit = 63
maxLen = 1
maxElement = nums[0]
minElement = nums[0]
windowStart = 0
windowEnd = 0
for index,num in enumerate(nums):
    # 在新元素比原先最小元素小的情况下
    if num < minElement:
        minElement = num
        # 在新元素 + limit 还比原先最大元素小的情况下
        if num + limit < maxElement:
            # 然后找出新滑动窗口的起始位置
            P = [0] # P为前缀数组
            maxValue = 0
            for i in range(0,index + 1):
                if minElement + limit < nums[i]:
                    P.append(P[-1] + 1)
                    maxValue += 1
                else:
                    P.append(P[-1])
            windowStart = bisect.bisect_left(P, maxValue)
            # 找到新滑动窗口的最大值
            maxElement = 0
            for i in range(windowStart,index + 1):
                if(nums[i] > maxElement):
                    maxElement = nums[i]
    # 在新元素比原先最大元素大的情况下
    elif num > maxElement:
        maxElement = num
        # 在新元素 - limit 还比原先最小元素大的情况下
        if num - limit > minElement:
            # 然后找出新滑动窗口的起始位置
            P = [0]  # P为前缀数组
            maxValue = 0
            for i in range(0, index + 1):
                if maxElement - limit > nums[i]:
                    P.append(P[-1] + 1)
                    maxValue += 1
                else:
                    P.append(P[-1])
            windowStart = bisect.bisect_left(P, maxValue)
            # 找到新滑动窗口的最小值
            minElement = nums[windowStart]
            # print(min,windowStart,index,minElement)
            for i in range(windowStart, index + 1):
                # print(nums[i])
                if (nums[i] <= minElement):
                    minElement = nums[i]
    windowEnd += 1
    if windowEnd - windowStart > maxLen:
        maxLen = windowEnd - windowStart
    print(windowStart, windowEnd,nums[windowStart:windowEnd], maxElement, minElement, maxLen)
print(maxLen)





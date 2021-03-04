nums = [10,9,2,5,3,7,101,102,103,7,19]
d = []
for n in nums:
    # 如果d为空或者最后一个数比n小，直接加入
    if not d or n > d[-1]:
        d.append(n)
    # 否则找到他在数组中应该出现的位置，替换原数
    else:
        l, r = 0, len(d) - 1
        loc = r
        # 二分查找确定loc
        while l <= r:
            mid = (l + r) // 2
            if d[mid] >= n:
                loc = mid
                r = mid - 1
            else:
                l = mid + 1
        d[loc] = n
    print(d)
print(len(d))



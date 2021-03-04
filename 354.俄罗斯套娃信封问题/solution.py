from bisect import bisect
from typing import List
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        n = len(envelopes)

        # python lambda表达式用法
        # 1.lambda表达式一般用法
        # add = lambda x, y: x + y
        # print(add(10, 20))  # >> 30

        # 2.lambda表达式在sort函数中的用法
        # 假如a是一个由元组构成的列表，对该列表进行排序时，我们需要用到参数key，也就是关键词，
        # 如下面代码所示，lambda是一个匿名函数，是固定写法；x表示匿名函数的输入，即列表中的一个元素，
        # 在这里，表示一个元组，x只是临时起的一个名字，你可以使用任意的名字；x[0]表示匿名函数的输出，
        # 即元组里的第一个元素，即key = x[0]；所以这句命令的意思就是按照列表中第一个元素进行排序
        # a = [('b', 4), ('a', 12), ('d', 7), ('h', 6), ('j', 3)]
        # a.sort(key=lambda x: x[0])
        # print(a) >> [('a', 12), ('b', 4), ('d', 7), ('h', 6), ('j', 3)]

        # 扩展一下：a.sort(key=lambda x: （x[0]，x[1]）)表示先按照x[0]
        # 升序排序（默认升序，如果需要降序要加负号）然后对于相同的x[0]，按照x[1]升序排序
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        f = [envelopes[0][1]]
        for i in range(1, n):
                # 如果最后一个数比i小，直接加入
            if envelopes[i][1] > f[-1]:
                f.append(envelopes[i][1])
            else:
                # 二分查找确定loc
                index = bisect.bisect_left(f, envelopes[i][1])
                f[index] = envelopes[i][1]

        return len(f)







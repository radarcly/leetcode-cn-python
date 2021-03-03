from typing import List
# 方法一：遍历 与 统计
# 这个应该是最容易想到的方法，遍历从 0 到 num 的每个数字，统计每个数字的二进制中 1 的个数。

# class Solution:
#     def countBits(self, num: int) -> List[int]:
#         res = []
#         for i in range(num + 1):
#             res.append(bin(i).count("1"))
#         return res

# 时间复杂度： O(N * sizeof(int))
# 空间复杂度：O(1)，返回数组不计入空间复杂度中


# 方法二：递归
# 把第 i 个数分成两种情况：

# 如果 i 是偶数，那么它的二进制 1 的位数与 i/2 的二进制 1 的位数相等；因为偶数的二进制末尾是 0，右移一位等于 i/2，而二进制中 1 的个数没有变化。
# 如果 i 是奇数，那么它的二进制 1 的位数 = i - 1 的二进制位数 + 1；因为奇数的二进制末尾是 1，如果把末尾的 1 去掉就等于 i - 1。
#               又 i - 1 是偶数，所以奇数 i 的二进制 1 的个数等于 i/2中二进制 1 的位数 +1.
# 通过上面的分析我们可以看出可以根据递归解决。

# class Solution(object):
#     def countBits(self, num):
#         res = []
#         for i in range(num + 1):
#             res.append(self.count(i))
#         return res
#
#     def count(self, num):
#         if num == 0:
#             return 0
#         if num % 2 == 1:
#             return self.count(num - 1) + 1
#         return self.count(num // 2)

# 时间复杂度： O(N ^ 2)，因为遍历了一次，每次求解最多需要递归 N/2次。
# 空间复杂度：O(N)，递归需要调用系统栈，栈的大小最多为 N/2。

# 方法三 记忆化搜索
# 在上面递归解法中，其实有很多重复的计算，比如当 i = 8 的时候，需要求 i=4,2,1,0 的情况，而这些取值已经计算过了，此时可以使用记忆化搜索。
# 所谓记忆化搜索，就是在每次递归函数结束的时候，把计算结果保存起来。这样的话，如果下次递归的时候遇到了同样的输入，则直接从保存的结果中直接查询并返回，不用再次递归。
# 举个例子，比如 i = 8 的时候，需要求 i = 4 的情况，而 i = 4 的情况在之前已经计算过了，因此直接返回 memo[4] 即可。

# class Solution(object):
#     def countBits(self, num):
#         self.memo = [0] * (num + 1)
#         res = []
#         for i in range(num + 1):
#             res.append(self.count(i))
#         return res
#
#     def count(self, num):
#         if num == 0:
#             return 0
#         if self.memo[num] != 0:
#             return self.memo[num]
#         if num % 2 == 1:
#             res = self.count(num - 1) + 1
#         else:
#             res = self.count(num // 2)
#         self.memo[num] = res
#         return res

# 时间复杂度：O(N)，因为遍历了一次，每次求解都可以从之前的记忆化结果中找到。
# 空间复杂度：O(N)，用到了辅助的空间保存结果，空间的结果是 O(N)。

# 其实上面这个记忆化搜索的方法也可以不用 memo 数组，直接利用 res 保存结果。

# 方法四 动态规划
# 其实很多时候，动态规划的方法都是从记忆化搜索中优化出来的。本题也可以如此。
# 方法三在记忆化搜索过程中，我们看到其实每次调用递归函数的时候，递归函数只会运行一次，就被 memo 捕获并返回了。那么其实可以去除递归函数，直接从 res 数组中查结果。
# 同时，优化了一下转移方程的表达式为 answer[i] = answer[i >> 1] + (i & 1) 。
# 于是得到下面的动态规划的方案。

class Solution:
    def countBits(self, num):
        res = [0] * (num + 1)
        for i in range(1, num + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res

# 时间复杂度： O(N)O(N)，因为遍历了一次。
# 空间复杂度：O(1)O(1)，返回结果占用的空间不计入空间复杂度中。









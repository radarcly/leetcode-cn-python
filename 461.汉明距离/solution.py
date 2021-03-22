#方法二：移位
# class Solution(object):
#     def hammingDistance(self, x, y):
#         """
#         :type x: int
#         :type y: int
#         :rtype: int
#         """
#         xor = x ^ y
#         distance = 0
#         while xor:
#             # mask out the rest bits
#             if xor & 1:
#                 distance += 1
#             xor = xor >> 1
#         return distance

#方法三 布赖恩·克尼根算法
class Solution:
    def hammingDistance(self, x, y):
        xor = x ^ y
        distance = 0
        while xor:
            distance += 1
            # remove the rightmost bit of '1'
            xor = xor & (xor - 1)
        return distance


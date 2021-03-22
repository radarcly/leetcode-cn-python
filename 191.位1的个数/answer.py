### 方法一 循环检查二进制位
class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        for i in range(32):
            if n & (1 << i):
                ret += 1
        return ret

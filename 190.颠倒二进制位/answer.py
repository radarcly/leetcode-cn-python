class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        for i in range(32):
            ret = ret << 1
            if n & (1 << i):
                ret += 1
        return ret
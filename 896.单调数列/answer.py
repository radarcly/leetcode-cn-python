class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) == 1:
            return True

        flag = 0
        for i in range(1,len(A)):
            tmp = A[i] - A[i-1]
            if flag == 0:
                if tmp > 0:
                    flag = 1
                elif tmp < 0:
                    flag = -1
            elif tmp * flag < 0:
                return False
        return True
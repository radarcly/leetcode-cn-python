class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])
        ret = []
        for i in range(n):
            ret.append([])
            for j in range(m):
                ret[i].append(matrix[j][i])
        return ret
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        # 其实不需要这个dict(),只需将每个元素与左上角元素做比较即可
        mp = dict()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i - j in mp:
                    if mp[i-j] != matrix[i][j]:
                        return False
                else :
                    mp[i-j] = matrix[i][j]

        return True
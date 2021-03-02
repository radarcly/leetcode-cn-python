class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        row = len(matrix)
        if row > 0:
            col = len(matrix[0])
            self.nums = [[]]
            for i in range(col + 1):
                self.nums[0].append(0)
            for i in range(row):
                self.nums.append([])
                self.nums[i + 1].append(0)
                row_sum = 0
                for j in range(col):
                    row_sum += matrix[i][j]
                    self.nums[i + 1].append(self.nums[i][j + 1] + row_sum)


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.nums[row2 + 1][col2 + 1] - self.nums[row1][col2 + 1] - self.nums[row2 + 1][col1] + self.nums[row1][col1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
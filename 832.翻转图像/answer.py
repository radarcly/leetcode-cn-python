A = [[1,1,0],[1,0,1],[0,0,0]]
row = len(A)
col = len(A[0])
# ret = [[0] * col] * row # 错误的构造方法，会导致list中所有元素都指向同一个，是一种浅拷贝
ret = []
for i in range(row):
    ret.append([])
    for j in range(col):
        # print(1 - A[i][col-j-1])
        ret[i].append(1 - A[i][col-j-1])
print(ret)
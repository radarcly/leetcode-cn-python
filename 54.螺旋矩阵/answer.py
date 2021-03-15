# 输入矩阵
matrix = [[7],[9],[6]]
# 返回值
ret = []
# 矩阵行数
m = len(matrix)
# 矩阵列数
n = len(matrix[0])
i = 0
j = m-1
x = 0
y = n-1
while i < j and x < y:
    # 遍历上方
    for k in range(x, y + 1):
        ret.append(matrix[i][k])
    # 遍历右方
    for k in range(i + 1, j):
        ret.append(matrix[k][y])
    # 遍历下方
    for k in range(y, x-1, -1):
        ret.append(matrix[j][k])
    # 遍历左方
    for k in range(j - 1, i, -1):
        ret.append(matrix[k][x])
    # 更新 i,j,x,y
    i += 1
    j -= 1
    x += 1
    y -= 1
#补充剩余
if i == j:
    for k in range(x, y + 1):
        ret.append(matrix[i][k])
elif x == y:
    for k in range(i, j + 1):
        ret.append(matrix[k][x])
    print(ret)



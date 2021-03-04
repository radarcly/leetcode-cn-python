envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
n = len(envelopes)

# 首先我们将所有的信封按照w值第一关键字升序、hh 值第二关键字降序进行排序；
# (之所以高度降序是因为同宽度只能取一个，高度降序就避免了取多个同高度信封的可能)
# 随后我们就可以忽略w维度，求出h维度的最长严格递增子序列，其长度即为答案。

envelopes.sort(key=lambda x: (x[0], -x[1]))
f = [1] * n
for i in range(n):
    for j in range(i):
        if envelopes[j][1] < envelopes[i][1]:
            f[i] = max(f[i], f[j] + 1)
print(f)
print(max(f))


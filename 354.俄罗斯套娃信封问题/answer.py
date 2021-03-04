envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
n = len(envelopes)
# 宽度升序，高度降序
envelopes.sort(key=lambda x: (x[0], -x[1]))
f = [1] * n
for i in range(n):
    for j in range(i):
        if envelopes[j][1] < envelopes[i][1]:
            f[i] = max(f[i], f[j] + 1)
print(f)
print(max(f))


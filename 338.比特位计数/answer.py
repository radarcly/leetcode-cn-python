import math
ret = [0]
for i in range(1, 6):
    k = math.floor(math.log(i,2))
    ret.append(1 + ret[i - 2 ** k])
print(ret)
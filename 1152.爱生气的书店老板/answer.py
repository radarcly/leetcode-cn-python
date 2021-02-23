customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
X = 3

# 计算初始[0:X] sum 和 max值
# sum值统计所有老板不生气时候服务满意的客户数量
# max值统计使得老板生气变不生气后最多服务满意的客户数量
# tmp值统计向右滑动时使得老板生气变不生气后服务满意的客户数量，如果大于max值，则对max重新赋值
sum = max = 0
for i in range(X):
    if grumpy[i] == 1:
        max += customers[i]
    else:
        sum += customers[i]
tmp = max

# 向右滑动从X滑动至最末元素
for i in range(X, len(customers)):
    if grumpy[i] == 0:
        sum += customers[i]
    else:
        tmp += customers[i]
    if grumpy[i - X] == 1:
        tmp -= customers[i - X]
    if tmp > max:
        max = tmp

print(sum + max)

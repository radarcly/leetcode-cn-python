# 方法一 不定长拉链数组
# class MyHashSet:
#
#     def __init__(self):
#         self.buckets = 1009
#         self.table = [[] for _ in range(self.buckets)]
#
#     def hash(self, key):
#         return key % self.buckets
#
#     def add(self, key):
#         hashkey = self.hash(key)
#         if key in self.table[hashkey]:
#             return
#         self.table[hashkey].append(key)
#
#     def remove(self, key):
#         hashkey = self.hash(key)
#         if key not in self.table[hashkey]:
#             return
#         self.table[hashkey].remove(key)
#
#     def contains(self, key):
#         hashkey = self.hash(key)
#         return key in self.table[hashkey]

# 方法二 超长数组
# 能使用超大数组来解决本题是因为输入数据的范围在 0<=key<=10的6次方。因此我们只需要 10^6 +1大小的数组，就能让每个数据都有一个单独的索引，不会有 key 的碰撞问题。
# 因为对于 HashSet 来说，我们只需要关注一个 key 是否存在，而不是 key:value 形式的 HashMap，因此，我们把数组的元素设计成 bool 型的，
# 当某个 key 的对应的数组中的位置取值为 true 说明该 key 存在，取值为 false，说明该 key 不存在。
# 优点：查找和删除的性能非常快，只用访问 1 次数组；
# 缺点：使用了非常大的空间，当元素范围很大时，无法使用该方法；当存储的元素个数较少时，性价比极低；需要预知数据的取值范围。
# class MyHashSet:
#     def __init__(self):
#         self.set = [False] * 1000001
#
#     def add(self, key):
#         self.set[key] = True
#
#     def remove(self, key):
#         self.set[key] = False
#
#     def contains(self, key):
#         return self.set[key]

# 方法三 定长拉链数组
# 这个方法本质上就是把 HashSet 设计成一个 M ∗ N 的二维数组。第一个维度用于计算 hash 分桶，第二个维度寻找 key 存放具体的位置。
# 用了一个优化：第二个维度的数组只有当需要构建时才会产生，这样可以节省内存。
#
# 优点：两个维度都可以直接计算出来，查找和删除只用两次访问内存。
# 缺点：需要预知数据范围，用于设计第二个维度的数组大小。
#

class MyHashSet:

    def __init__(self):
        self.buckets = 1000
        self.itemsPerBucket = 1001
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def pos(self, key):
        return key // self.buckets

    def add(self, key):
        hashkey = self.hash(key)
        if not self.table[hashkey]:
            self.table[hashkey] = [0] * self.itemsPerBucket
        self.table[hashkey][self.pos(key)] = 1

    def remove(self, key):
        hashkey = self.hash(key)
        if self.table[hashkey]:
            self.table[hashkey][self.pos(key)] = 0

    def contains(self, key):
        hashkey = self.hash(key)
        return (self.table[hashkey] != []) and (self.table[hashkey][self.pos(key)] == 1)


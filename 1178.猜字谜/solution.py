from future.moves import collections

words = ["aaaa","asas","able","ability","actt","actor","access"]
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
frequency = collections.Counter()  # 计数器
for word in words:
    mask = 0
    for ch in word:
        mask |= (1 << (ord(ch) - ord("a")))  # ord()函数获取ASCILL码 << 左移运算符 |= 位或运算符
    if str(bin(mask)).count("1") <= 7:  # bin()函数获取数字的二进制表示 无视包含大于7个字母的word
        frequency[mask] += 1   # 把包含相同字母的数字放在key-value的计数器中
ans = list()

# 对于每个puzzle 要枚举他包含的子集，然后将frequency[子集元素]求和
for puzzle in puzzles:
    total = 0
    # 枚举子集方法一
    # for choose in range(1 << 6):  # 1 << 6 = 2的6次方 64因为puzzle的长度必定为7且第一个元素必定在word中出现，每个元素不重复
    #     mask = 0
    #     # 20-22行 找出六位中出现1的位数将其转换为对应mask
    #     for i in range(6):
    #         if choose & (1 << i):  #
    #             mask |= (1 << (ord(puzzle[i + 1]) - ord("a")))
    #     # 第一个元素必定在word中出现
    #     mask |= (1 << (ord(puzzle[0]) - ord("a")))
    #     if mask in frequency:
    #         total += frequency[mask]

    # 枚举子集方法二
    mask = 0
    for i in range(1, 7):
        mask |= (1 << (ord(puzzle[i]) - ord("a")))

    subset = mask
    while subset:
        s = subset | (1 << (ord(puzzle[0]) - ord("a")))
        if s in frequency:
            total += frequency[s]
        subset = (subset - 1) & mask

    # 在枚举子集的过程中，要么会漏掉全集 mask，要么会漏掉空集
    # 这里会漏掉空集，因此需要额外判断空集
    if (1 << (ord(puzzle[0]) - ord("a"))) in frequency:
        total += frequency[1 << (ord(puzzle[0]) - ord("a"))]

    ans.append(total)



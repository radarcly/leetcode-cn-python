# 通过9/10个测试用例 第十个测试用例超时
words = ["aaaa","asas","able","ability","actt","actor","access"]
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
ret = []
for puzzle in puzzles:
    number = 0
    for word in words:
        if puzzle[0] not in word:
            continue
        else:
            flag = True
            for letter in word:
                if letter not in puzzle:
                    flag = False
                    continue
            if(flag):
                number += 1
    ret.append(number)
print(ret)

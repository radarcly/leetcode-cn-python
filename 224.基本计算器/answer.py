s = "(1+(4+5+2)-3)+(6+8)"
ops = []
ops.append(1)
sign = 1
ret = 0
i = 0
while i < len(s):
    if s[i] == " ":
        i += 1
    elif s[i] == "+":
        sign = ops[-1]
        i += 1
    elif s[i] == "-":
        sign = -ops[-1]
        i += 1
    elif s[i] == "(":
        ops.append(sign)
        i += 1
    elif s[i] == ")":
        ops.pop()
        i += 1
    else:
        num = 0
        while i < len(s) and s[i].isdigit():
             num = num  * 10 + int(s[i])
             i += 1
        ret += sign * num
print(ret)
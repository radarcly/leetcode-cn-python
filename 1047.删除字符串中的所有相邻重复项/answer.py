S = "abbaca"
ret = []
for ch in S:
    if ret and ch == ret[-1]:
        ret.pop()
    else:
        ret.append(ch)
print("".join(ret))


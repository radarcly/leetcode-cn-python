def partition(s):
    res = []
    path = []
    dfs_backtrace(s,res,path)
    return res


def dfs_backtrace(s,res,path):
    n = len(s)
    if n == 0:
        res.append(path[:])
    for j in range(n):
        if isPalindrome(s[:j + 1]):
            path.append(s[:j + 1])
            dfs_backtrace(s[j + 1:],res,path)
            path.pop(-1)


def isPalindrome(s):
    return s == s[::-1]


print(partition("aab"))

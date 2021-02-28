# s = "ababacb"
# k = 3

# s = "aaabb"
# k = 3

s = "ababbc"
k = 2

def longestSubstringHelper(s, k, lettersLasted):
    if(len(s) < k):
        return 0
    letters = []
    mp = {}
    for letter in s:
        if letter in mp:
            mp[letter] += 1
        else:
            mp[letter] = 1
    for key, value in mp.items():
        if value >= k:
            letters.append(key)
    if len(letters) == len(lettersLasted):
        return len(s)
    else:
        start = end = 0
        maxLen = 0
        for index, letter in enumerate(s):
            if letter not in letters:
                ret = longestSubstringHelper(s[start:end], k, letters)
                if ret > maxLen:
                    maxLen = ret
                start = index + 1
            end += 1
        ret = longestSubstringHelper(s[start:end], k, letters)
        if ret > maxLen:
            maxLen = ret
        return maxLen


mp = {}
for letter in s:
    if letter in mp:
        mp[letter] += 1
    else:
        mp[letter] = 1

letters = []
for key, value in mp.items():
    if value >= k:
        letters.append(key)


start = end = 0
maxLen = 0
for index, letter in enumerate(s):
    if letter not in letters:
        ret = longestSubstringHelper(s[start:end],k,letters)
        if ret > maxLen:
            maxLen = ret
        start = index + 1
    end += 1
ret = longestSubstringHelper(s[start:end],k,letters)
if ret > maxLen:
    maxLen = ret
print(maxLen)





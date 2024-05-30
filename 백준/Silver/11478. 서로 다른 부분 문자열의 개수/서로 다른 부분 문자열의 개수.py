from sys import stdin

s = stdin.readline().rstrip()

def getSuffixArray(s):
    suffixes = sorted([(s[i:], i) for i in range(len(s))])
    return [suffix[1] for suffix in suffixes]

def getLcpArray(s, suffixArray):
    n = len(s)

    rank = [0] * n
    lcp = [0] * n

    for i, suffix in enumerate(suffixArray):
        rank[suffix] = i

    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = suffixArray[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1

    return lcp
     
suffixArray = getSuffixArray(s)
lcp = getLcpArray(s, suffixArray)

n = len(s)
numSubstrings = 0
for i in range(n):
    numSubstrings += n - suffixArray[i] - lcp[i]

print(numSubstrings)
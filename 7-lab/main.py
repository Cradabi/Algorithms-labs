import math
from collections import defaultdict

nums = []

for num in range(3,10100,2):
    if len(nums) < 500:
        if all(num%i!=0 for i in range(3,int(math.sqrt(num))+1, 2)):
            nums.append(num)
    else:
        break

primestr = ''.join(map(str, nums))

def naive(text, key):
    cnt = 0
    n = len(text)
    m = len(key)
    for x in range(0, n-m+1):
        if text[x:x+m] == key:
            cnt += 1
    return cnt

def rabin_karp(s, p, d=10, q=101):
    cnt = 0
    n = len(s)
    m = len(p)
    h = pow(d, m-1) % q
    hash_s = 0
    hash_p = 0
    for i in range(m):
        hash_p = (d*hash_p + ord(p[i])) % q
        hash_s = (d*hash_s + ord(s[i])) % q
    for i in range(n-m+1):
        if hash_s == hash_p:
            if s[i:i+m] == p:
                cnt +=1
        if i < n-m:
            hash_s = (d*(hash_s - ord(s[i])*h)+ord(s[i+m])) % q
    return cnt

def boyer_moore_horspool(text, pattern):
    m = len(pattern)
    n = len(text)

    if m > n:
        return -1

    skip = defaultdict(lambda: m)
    cnt = 0

    for k in range(m - 1):
        skip[ord(pattern[k])] = m - k - 1

    k = m - 1

    while k < n:
        j = m - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            cnt +=1

        k += skip[ord(text[k])]

    return cnt

def func_prefix(s):
    l = len(s)
    P = [0]*l
    i, j = 0, 1
    while j < l :
        if s[i] == s[j]:
            P[j] = i + 1
            i += 1
            j += 1

        elif i:
            i = P[i - 1]
        else:
            P[j] = 0
            j += 1
    return P

def kmp(text, sub):
    sub_len = len(sub)
    text_len = len(text)
    if not text_len or sub_len > text_len:
        return []
    P = func_prefix(sub)
    cnt = 0
    i = j = 0
    while i < text_len:
        if text[i] == sub[j]:
            if j == sub_len - 1:
                cnt +=1
                j = P[j]
            else:
                j += 1
            i += 1
        elif j:
            j = P[j-1]
        else:
            i += 1
    return cnt

maxcnt = 0
mostfreqnum = ''

for i in range(10, 99):
    a = naive(primestr, str(i))
    if a > maxcnt:
        mostfreqnum = str(i)
        maxcnt = a

print(mostfreqnum, maxcnt)

maxcnt = 0
mostfreqnum = ''

for i in range(10, 99):
    a = boyer_moore_horspool(primestr, str(i))
    if a > maxcnt:
        mostfreqnum = str(i)
        maxcnt = a

print(mostfreqnum, maxcnt)

maxcnt = 0
mostfreqnum = ''

for i in range(10, 99):
    a = kmp(primestr, str(i))
    if a > maxcnt:
        mostfreqnum = str(i)
        maxcnt = a

print(mostfreqnum, maxcnt)

maxcnt = 0
mostfreqnum = ''

for i in range(10, 99):
    a = rabin_karp(primestr, str(i))
    if a > maxcnt:
        mostfreqnum = str(i)
        maxcnt = a

print(mostfreqnum, maxcnt)

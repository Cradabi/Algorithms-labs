def subStrHash(s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
    start = 0
    withmod = 0
    m = (power ** k) % modulo
    sum = 0
    if len(s) >= k:
        for i in range(k):
            sum = sum + (ord(s[i]) - 96) * (power ** i)
        withmod = sum % modulo
        if withmod == hashValue:
            return s[:k]

    for i in range(1, len(s) - k + 1):
        sum = sum - (ord(s[i - 1]) - 96)
        sum = sum // power
        sum += (ord(s[i + k - 1]) - 96) * (power ** (k - 1))
        withmod = sum % modulo
        if withmod == hashValue:
            start = i
            return s[start:start + k]
    return ''

print(subStrHash("leetcode", 7, 20, 2, 0))
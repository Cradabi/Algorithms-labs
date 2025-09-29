import math
from collections import defaultdict


def generate_odd_primes(count):
    primes = []
    for num in range(3, 10_000, 2):
        if len(primes) >= count:
            break
        if all(num % i != 0 for i in range(3, int(math.sqrt(num)) + 1, 2)):
            primes.append(num)
    return primes


def primes_to_string(primes):
    return ''.join(map(str, primes))



def naive(text, key):
    n, m = len(text), len(key)
    return sum(text[i:i + m] == key for i in range(n - m + 1))


def rabin_karp(s, p, d=10, q=101):
    cnt = 0
    n, m = len(s), len(p)
    h = pow(d, m - 1) % q
    hash_s = hash_p = 0

    for i in range(m):
        hash_p = (d * hash_p + ord(p[i])) % q
        hash_s = (d * hash_s + ord(s[i])) % q

    for i in range(n - m + 1):
        if hash_s == hash_p and s[i:i + m] == p:
            cnt += 1
        if i < n - m:
            hash_s = (d * (hash_s - ord(s[i]) * h) + ord(s[i + m])) % q

    return cnt


def boyer_moore_horspool(text, pattern):
    m, n = len(pattern), len(text)
    if m > n:
        return 0

    skip = defaultdict(lambda: m)
    for k in range(m - 1):
        skip[ord(pattern[k])] = m - k - 1

    cnt = 0
    k = m - 1
    while k < n:
        j, i = m - 1, k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            cnt += 1
        k += skip[ord(text[k])]
    return cnt


def func_prefix(s):
    l = len(s)
    P = [0] * l
    i, j = 0, 1
    while j < l:
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
    sub_len, text_len = len(sub), len(text)
    if not text_len or sub_len > text_len:
        return 0
    P = func_prefix(sub)
    cnt = i = j = 0
    while i < text_len:
        if text[i] == sub[j]:
            if j == sub_len - 1:
                cnt += 1
                j = P[j]
            else:
                j += 1
            i += 1
        elif j:
            j = P[j - 1]
        else:
            i += 1
    return cnt


def find_most_frequent_substring(text, search_fn, start=10, end=99):
    maxcnt = 0
    mostfreqnum = ''
    for num in range(start, end):
        pattern = str(num)
        cnt = search_fn(text, pattern)
        if cnt > maxcnt:
            maxcnt = cnt
            mostfreqnum = pattern
    return mostfreqnum, maxcnt


def run_all_algorithms():
    primes = generate_odd_primes(500)
    primestr = primes_to_string(primes)

    algorithms = {
        "Naive": naive,
        "Boyer-Moore-Horspool": boyer_moore_horspool,
        "KMP": kmp,
        "Rabin-Karp": rabin_karp
    }

    results = {}

    for name, func in algorithms.items():
        pattern, count = find_most_frequent_substring(primestr, func)
        results[name] = (pattern, count)

    return results


if __name__ == "__main__":
    results = run_all_algorithms()
    for alg, (pattern, count) in results.items():
        print(f"{alg}: {pattern} -> {count}")
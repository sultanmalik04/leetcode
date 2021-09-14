def lengthOfLongestSubstring(s: str) -> int:
    i = 0
    j = 0
    n = len(s)
    window_start = -1
    windowlen = 0
    maxWindowlen = 0
    mp = {}
    while j <= n-1:
        ch = s[j]
        if ch in mp and mp[ch] >= i:
            i = mp[ch]+1
            windowlen = j - i
        mp[ch] = j 
        windowlen += 1
        j += 1
        if windowlen > maxWindowlen:
            maxWindowlen = windowlen
            window_start = i
    print(maxWindowlen)
    return s[window_start:maxWindowlen]

print(lengthOfLongestSubstring('abcabcd'))
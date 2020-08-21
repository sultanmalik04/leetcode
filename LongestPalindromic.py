class Solution:
    def longestPalindrome(self, s: str) -> str:
        substring = [s[i:j] for i in range(len(s))
                     for j in range(i + 1, len(s) + 1)]
        palindrom = ''
        for i in substring:
            if i[::-1] == i:
                if len(i) > len(palindrom):
                    palindrom = i
        return palindrom

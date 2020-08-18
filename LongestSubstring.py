class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l_index = [-1]*256
        i = 0
        res = 0
        for j in range(len(s)):
            i = max(i, l_index[ord(s[j])] + 1)
            res = max(res, j - i + 1)
            l_index[ord(s[j])] = j
        return res

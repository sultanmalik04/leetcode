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
            i = max(i, l_index[ord(s[j])] + 1) # here i will be update only when characters get repeated so basically i stores starting index of window 
            res = max(res, j - i + 1) # here we will calculate the length of window 
            l_index[ord(s[j])] = j 
        return res

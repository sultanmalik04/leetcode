
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        rev_no = 0
        while temp > 0:
            d = temp % 10
            rev_no = rev_no*10 + d
            temp //= 10
        if x == rev_no:
            return True
        else:
            return False

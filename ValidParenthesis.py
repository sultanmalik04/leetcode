class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            if s[i] == ')' or s[i] == ']' or s[i] == '}':
                if len(stack) == 0:
                    return False
                else:
                    temp = stack.pop()
                    if s[i] == ')' and (temp == '{' or temp == '['):
                        return False
                    elif s[i] == ']' and (temp == '{' or temp == '('):
                        return False
                    elif s[i] == '}' and (temp == '(' or temp == '['):
                        return False
        if len(stack) > 0:
            return False
        else:
            return True

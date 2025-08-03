class Solution(object):
    def isValid(self, s):

        stack = []
        mapping = {')': '(', ']': '[', '}':'{'}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if stack and stack[-1] == mapping[char]:
                    stack.pop()
                else:
                    return False
        return not stack
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matchOpen = {')' : '(', ']':'[', '}' : '{'}

        for c in s:
            if c in matchOpen:
                if stack and stack[-1] == matchOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
        
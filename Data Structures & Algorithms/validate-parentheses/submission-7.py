class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map_close = {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif c in [')', '}', ']']:
                if len(stack) == 0:
                    return False
                if stack[-1] == map_close[c]:
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        return True
        
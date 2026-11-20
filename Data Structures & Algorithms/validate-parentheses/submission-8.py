class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')': '(','}':'{', ']':'['}
        stack = []

        for p in s:
            if p not in bracket_map:
                stack.append(p)
                continue
            if not stack or stack[-1] != bracket_map[p]:
                return False
            stack.pop()
        return not stack
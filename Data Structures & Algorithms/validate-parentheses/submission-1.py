class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in pairs.values():
                stack.append(c)
            else:
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()

        return len(stack) == 0
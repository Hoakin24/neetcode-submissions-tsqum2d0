class Solution:
    def isValid(self, s: str) -> bool:
        print(len(s))
        if len(s) <= 1: return False

        pairings = {
            '}': '{',
            ')': '(',
            ']': '[',
        }
        stack = []
        for i in range(len(s)):
            if s[i] in pairings.values():
                stack.append(s[i])
            elif len(stack) <= 0 or stack.pop() != pairings[s[i]]:
                return False
            

        return len(stack) == 0
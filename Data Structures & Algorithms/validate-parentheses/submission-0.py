class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        comb = {')':'(', '}':'{', ']':'['}
        for i in range(len(s)):
            if s[i] in '({[': 
                stack.append(s[i])
            else: 
                if not stack or stack[-1] != comb[s[i]]: 
                    return False 
                stack.pop()    
        return len(stack) == 0
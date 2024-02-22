class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braket = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char in braket.values():
                stack.append(char)
            else:
                if not stack or stack.pop() != braket[char]:
                    return False
        return not stack
                

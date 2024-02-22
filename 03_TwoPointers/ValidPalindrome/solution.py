import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return clean_text == clean_text[::-1]
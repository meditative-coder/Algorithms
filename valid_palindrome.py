import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(re.split("[^a-zA-Z0-9]*", s))
        s = s.lower()
        return s==s[::-1]

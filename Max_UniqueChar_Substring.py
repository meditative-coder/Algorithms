class Solution:
    def maxPower(self, s: str) -> int:
        i = 0
        n = len(s)
        if s == "":
            return 0
        max_count = 1
        while i < n:
            count = 1
            j = i
            while j+1 < n and s[j]==s[j+1]:
                count = count + 1
                j = j + 1
            i = j
            i = i+1
            if count > max_count:
                max_count = count
                
        return max_count

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(needle)
        for i in range(len(haystack)):
            if haystack[i:n+i]==needle:
                return i
        else:
            return -1
            
    
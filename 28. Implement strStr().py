# 28. Implement strStr()

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Return the index of the first occurrence of needle in haystack,
         or -1 if needle is not part of haystack.
        """
        if not len(needle):
            return 0
        s = needle + '$' + haystack  
        n = len(s)
        z = [0 for _ in range(n)]
        left = right = 0 
        for index in range(1, n):
            x = min(z[index - left], right - index + 1) if index <= right else 0
            while x + index < n and s[x] == s[x + index]:
                x += 1
            z[index] = x
            if x == len(needle):
                return index - len(needle) - 1
            if x + index - 1 > right:
                left, right = index, x + index - 1
        return -1
        
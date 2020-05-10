# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Given a string, determine if it is a palindrome,
        considering only alphanumeric characters and ignoring cases.
        """
        filterString = [char.lower() for char in s if char.isalnum()] 
        return filterString[::-1] == filterString


sol = Solution()
res = sol.isPalindrome("race  car")
print(res)
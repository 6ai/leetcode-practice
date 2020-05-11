# 3. Longest Substring Without Repeating Characters

# O(n^2) time | O(1) space
class Solution:
    def isPalidrome(self, s) -> bool:
        return s[::-1] == s

    def longestPalidromeAtIndex(self, index: int, s: str) -> str:
        longestPalidrome = s[index]

        if index == 0:
            return longestPalidrome

        shift = 1
        currentSubstring = s[index - shift: index + shift + 1]
        while self.isPalidrome(currentSubstring) and shift <= index and index + shift < len(s):
            longestPalidrome = currentSubstring
            shift += 1
            currentSubstring = s[index - shift: index + shift + 1]
        
        shift = 1
        currentSubstring = s[index - shift: index + shift]
        while self.isPalidrome(currentSubstring) and shift <= index and index + shift - 1 < len(s):
            if len(currentSubstring) > len(longestPalidrome):
                longestPalidrome = currentSubstring
            shift += 1
            currentSubstring = s[index - shift: index + shift]

        return longestPalidrome
    
    def longestPalindrome(self, s: str) -> str:
        """
        Given a string s, find the longest palindromic substring in s.
        You may assume that the maximum length of s is 1000.
        """
        longestPalidrome = ''
        for index in range(len(s)):
            currentPalidrome = self.longestPalidromeAtIndex(index, s)
            if len(currentPalidrome) > len(longestPalidrome):
                longestPalidrome = currentPalidrome 
        return longestPalidrome

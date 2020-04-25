# 151. Reverse Words in a String
# Given an input string, reverse the string word by word.

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])


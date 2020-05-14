# 17. Letter Combinations of a Phone Number

class Solution:
    """
    Given a string containing digits from 2-9 inclusive,
     return all possible letter combinations that the number could represent.
    """
    def letterCombinationsHelper(self, mapping, index, digits, prefix, combinations):
        if not index < len(digits):
            combinations.append(prefix)
            return
        for char in mapping[digits[index]]:
            self.letterCombinationsHelper(mapping, index + 1, digits, prefix + char, combinations)

    def letterCombinations(self, digits: str) -> [str]:
        if not len(digits): 
            return []
        mapping = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', 
        '8': 'tuv', '9': 'wxyz'}
        combinations = []
        self.letterCombinationsHelper(mapping, 0, digits, '', combinations)
        return combinations


        
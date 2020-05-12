# 49. Group Anagrams

class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        """
        Given an array of strings, group anagrams together.
        """
        anagrams = dict()
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord in anagrams:
                anagrams[sortedWord].append(word)
            else:
                anagrams[sortedWord] = [word]
        return list(anagrams.values())

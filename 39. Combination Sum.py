# 39. Combination Sum

class Solution:
    def combinationSumHelper(self, candidates, combination, target, combinations):
        currentSum = sum(combination)
        if currentSum > target:
            return
        if currentSum == target:
            combinations.add(tuple(sorted(combination)))
            return
        for x in candidates:
            self.combinationSumHelper(candidates, combination + [x], target, combinations)

    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        combinations = set()
        self.combinationSumHelper(candidates, [], target, combinations)
        return combinations

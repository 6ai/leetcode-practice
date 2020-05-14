# 40. Combination Sum II

class Solution:
    def combinationSumHelper(self, candidates, combination, index, target, combinations):
        currentSum = sum(combination)
        if currentSum > target:
            return
        if currentSum == target:
            combinations.add(tuple(sorted(combination)))
            return
        for x in range(index, len(candidates)):
            self.combinationSumHelper(candidates, combination + [candidates[x]], x + 1, target, combinations)

    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        
        combinations = set()
        self.combinationSumHelper(candidates, [], 0, target, combinations)
        return combinations

# 22. Generate Parentheses

class Solution:
    """
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    """
    def generateParenthesisHelper(self, n, opened, closed, prefix, parenthesis):
        if n == opened and n == closed:
            parenthesis.append(prefix)
        if opened < n:
            self.generateParenthesisHelper(n, opened + 1, closed, prefix + '(', parenthesis)
        if opened > closed:
            self.generateParenthesisHelper(n, opened, closed + 1, prefix + ')', parenthesis)

    def generateParenthesis(self, n: int) -> [str]:
        parenthesis = []
        self.generateParenthesisHelper(n, 0, 0, '', parenthesis)
        return parenthesis

ret = Solution().generateParenthesis(3)
print(ret)
        
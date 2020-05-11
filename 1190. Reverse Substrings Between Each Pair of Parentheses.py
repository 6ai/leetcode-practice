# 1190. Reverse Substrings Between Each Pair of Parentheses

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for currentSymbol in s:
            if currentSymbol == ')':
                self.reverseLastAddedWord(stack)
            else:
                stack.append(currentSymbol)
        return ''.join(stack)

    def reverseLastAddedWord(self, stack):
        lastAddedWord = ''
        while True:
            currentSymbol = stack.pop()
            if currentSymbol == '(':
                break
            lastAddedWord += currentSymbol[::-1]
        stack.append(lastAddedWord)
            
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        :type tokens: List[str]
        :rtype: int
        """
        numbers = []
        for token in tokens:
            if token == "+":
                number = numbers.pop()
                numbers.append(numbers.pop() + number)
            elif token == "-":
                number = numbers.pop()
                numbers.append(numbers.pop() - number)
            elif token == "*":
                number = numbers.pop()
                numbers.append(numbers.pop() * number)
            elif token == "/":
                number = numbers.pop()
                numbers.append(int(numbers.pop() / number))
            else:
                numbers.append(int(token))
        return numbers[-1]
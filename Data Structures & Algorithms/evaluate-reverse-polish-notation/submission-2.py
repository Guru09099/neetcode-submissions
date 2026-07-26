class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens) == 0:
            return 0
        if len(tokens) == 1:
            return int(tokens[0])
        for i in range(len(tokens)):
            if stack and tokens[i] in "+-/*":
                b = int(stack.pop())
                a = int(stack.pop())
                if tokens[i] == '+':
                    total =  a + b
                elif tokens[i] == '-':
                    total = a - b
                elif tokens[i] == '*':
                    total = a * b
                elif tokens[i] == '/':
                    total = int(a / b)
                stack.append(total)
            else:
                stack.append(tokens[i])
        return total


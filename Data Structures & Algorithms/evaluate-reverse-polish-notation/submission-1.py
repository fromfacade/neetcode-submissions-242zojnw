class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for token in tokens:
            if token == '+':
                stk.append(stk.pop() + stk.pop())
            elif token == '-':
                stk.append(stk.pop() -  stk.pop())
            elif token == '/':
                a, b = stack.pop(), stack.pop()
                stk.append(int(float(b) / a))
            elif token == '*':
                stk.append(stk.pop() * stk.pop())

            else: 
                stk.append(int(token))

        return stk.pop()
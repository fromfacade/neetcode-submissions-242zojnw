class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            return 0

        res = []
        for token in tokens:
            if token == "+":
                ans = (res.pop()) + (res.pop())
                res.append(ans)
            elif token == "*":
                ans = (res.pop()) * (res.pop())
                res.append(ans)
            elif token == "-":
                a, b = res.pop(), res.pop()
                ans = (b - a)
                res.append(ans)
            elif token == "/":
                a, b = res.pop(), res.pop()
                ans = int(float(b)/ a)
                res.append(ans)
            else:
                res.append(int(token))
        
        return res[0]
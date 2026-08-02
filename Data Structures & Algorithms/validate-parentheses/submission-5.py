class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        pending = []

        for p in s:
            if p == ')' or p == '}' or p ==']':
                return False
            elem = s.pop()
            check = s.pop()
            if elem == '(':
                if check != ')':
                    pending.append(check)
                else:
                    continue
            elif elem == '{':
                if check != ')':
                    pending.append(check)
                else:
                    continue
            elif elem == '[':
                if check != ')':
                    pending.append(check)
                else:
                    continue
        if not pending:
            return True
        else:
            return False


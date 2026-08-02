class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        pending = []

        for p in s:
            elem = s.pop()
            if not s and pending:
                return False
            else:
                check = s.pop
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


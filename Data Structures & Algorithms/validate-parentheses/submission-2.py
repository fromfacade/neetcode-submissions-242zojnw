class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        pending = []

        for p in s:
            elem = s.pop()
            if elem == '(':
                check = s.pop()
                if check != ')':
                    pending.append(check)
                else:
                    continue
            elif elem == '{':
                check = s.pop()
                if check != ')':
                    pending.append(check)
                else:
                    continue
            elif elem == '[':
                check = s.pop()
                if check != ')':
                    pending.append(check)
                else:
                    continue
        if not pending:
            return True
        else:
            return False


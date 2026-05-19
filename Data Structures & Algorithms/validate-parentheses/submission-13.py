class Solution:
    def isValid(self, s: str) -> bool:
        pending = []

        pairs = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for p in s:
            if p in pairs:
                if not pending or pending[-1] != pairs[p]:
                    return False   
                else:
                    pending.pop()
            else:
                pending.append(p)
        return len(pending) == 0
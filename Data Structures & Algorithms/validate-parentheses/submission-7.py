class Solution:
    def isValid(self, s: str) -> bool:
        pending = []

        par = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for p in s:
            if p in par:
                if not pending or pending[-1] != par[p]:
                    return False
                pending.pop()
            else:    
                pending.append(p)
        
        return len(pending) == 0
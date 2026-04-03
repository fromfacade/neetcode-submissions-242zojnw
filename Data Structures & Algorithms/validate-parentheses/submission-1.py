class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {")":"(","]":"[","}":"{"}

        for elem in s:
            if elem in valid:
                if stack and stack[-1] == valid[elem]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(elem)
        return False if stack else True

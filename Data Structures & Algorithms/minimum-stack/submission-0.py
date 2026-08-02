class MinStack:

    def __init__(self):
        self.stack = list()
        self.mni = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mni.append(val)
        self.mni.sort()

    def pop(self) -> None:
        self.mni.pop(self.stack[-1])
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mni[0]

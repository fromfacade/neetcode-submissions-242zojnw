class MinStack():

    def __init__(self):
        self.stack = []
        self.mni = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.mni[-1] if self.mni else val)
        self.mni.append(val)

    def pop(self) -> None:
        self.mni.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mni[-1]

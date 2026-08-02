class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity


    def get(self, i: int) -> int:
        return self.arr[i - 1]

    def set(self, i: int, n: int) -> None:
        self.arr[i - 1] = n

    def pushback(self, n: int) -> None:
        #self.
        if self.size == self.capacity:
            self.resize()
        
        self.arr[self.size - 1] = n
        self.size += 1

    def popback(self) -> int:
        if self.size > 0:
            self.size -= 1
        return self.arr[self.size - 1]

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity
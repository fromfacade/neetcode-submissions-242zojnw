#doubly linked list node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        #make two dummy nodes, helps make things simpler and gets rid of some edge cases
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        newNode = Node(value)
        lastNode = self.tail.prev

        lastNode.next = newNode
        newNode.prev = lastNode
        newNode.next = self.tail
        self.tail.prev = newNode

    def appendleft(self, value: int) -> None:
        newNode = Node(value)
        firstNode = self.head.next

        firstNode.prev = newNode
        newNode.next = firstNode
        newNode.prev = self.head
        self.head.next = newNode
        #using what you learned from the video/code above, try implementing this yourself.

    def pop(self) -> int:
        if self.head.next == self.tail:
            return -1

        lastNode = self.tail.prev
        value = lastNode.value
        prevNode = lastNode.prev

        prevNode.next = self.tail
        self.tail.prev = prevNode

        return value 

        #maybe the next two as well?

    def popleft(self) -> int:
        if self.head.next == self.tail:
            return -1

        firstNode = self.head.next
        value = firstNode.value
        nxtNode = firstNode.next

        nxtNode.prev = self.head
        self.head.next = nxtNode

        return value
        
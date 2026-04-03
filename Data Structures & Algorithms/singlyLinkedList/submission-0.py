class ListNode:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

class LinkedList:
    
    def __init__(self):
        #dummy node?? helps with edge cases
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        #base case
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        
        return -1

        #traverse the list, and return the node at the i-th node


    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next
        self.head.next = newNode

        if not newNode.next:
            #if list was empty befor inserting
            self.tail = newNode

        #find where the head is, insert element there and set pointer to prev head

    def insertTail(self, val: int) -> None:
        #find where the tail is, insert element there and make tail pointer point to new tail
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        #locate node, and remove it by making the surrounding pointers point somewhere else
        curr = self.head
        i = 0

        while i < index and curr:
            #move curr to node before target node
            i += 1            
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True

        return False    

    def getValues(self) -> List[int]:
        #simply return the values of the linked list in a list
        curr = self.head.next
        res = []
        
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

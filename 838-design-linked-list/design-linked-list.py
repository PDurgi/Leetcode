class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        current = self.head
        start = 0
        while current:
            if start == index:
                return current.val
            current = current.next
            start += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        if index == self.length:
            self.addAtTail(val)
            return
        if index == 0:
            self.addAtHead(val)
            return
        new_node = Node(val)
        current = self.head
        start = 0
        prev = None
        while current:
            if start == index:
                break
            prev = current
            current = current.next
            start += 1
        prev.next = new_node
        new_node.next = current
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            start = 0
            prev = None
            while current:
                if start == index:
                    break
                prev = current
                current = current.next
                start += 1
            prev.next = current.next
        self.length -= 1

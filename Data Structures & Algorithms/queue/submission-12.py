class LinkNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class Deque:
    
    def __init__(self):
        self.left = self.right = None

    def isEmpty(self) -> bool:
        return self.left is None

    def append(self, value: int) -> None:
        newNode = LinkNode(value)
        if self.right is None:
            self.left = self.right = newNode
        else:
            self.right.next = newNode
            newNode.prev = self.right
            self.right = self.right.next

    def appendleft(self, value: int) -> None:
        newNode = LinkNode(value)
        if self.left is None:
            self.left = self.right = newNode
        else:
            self.left.prev = newNode
            newNode.next = self.left
            self.left = self.left.prev

    def pop(self) -> int:
        if self.right is None:
            return -1
        else:
            value = self.right.value
            self.right = self.right.prev
            if self.right is None:
                self.left = None
            else:
                self.right.next = None
            return value

    def popleft(self) -> int:
        if self.left is None:
            return -1
        else:
            value = self.left.value
            self.left = self.left.next
            if self.left is None:
                self.right = None
            else:
                self.left.prev = None
            return value
        

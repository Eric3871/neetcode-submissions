class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.left = self.right = None
    
    def enqueue(self, value):
        newNode = Node(value)
        
        if self.right:
            self.right.next = newNode
            self.right = self.right.next
        else:
            self.left = self.right = newNode
    
    def dequeue(self):
        if not self.left:
            return None
        
        value = self.left.value
        self.left = self.left.next
        if not self.left:
            self.right = None
        
        return value
    
    def isEmpty(self):
        return self.left is None

class MyStack:

    def __init__(self):
        self.stack1 = Queue()
        self.size = 0

    def push(self, x: int) -> None:
        self.stack1.enqueue(x)
        for x in range(self.size):
            self.stack1.enqueue(self.stack1.dequeue())
        self.size += 1

    def pop(self) -> int:
        self.size -= 1
        return self.stack1.dequeue()

        return self.stack1.dequeue()
    def top(self) -> int:
        return self.stack1.left.value

    def empty(self) -> bool:
        return self.stack1.isEmpty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
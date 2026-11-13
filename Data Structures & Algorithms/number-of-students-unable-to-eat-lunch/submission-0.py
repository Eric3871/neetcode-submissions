class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.left = self.right = None
    
    def enqueue(self, value):
        newNode = ListNode(value)
        
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

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = Queue()
        for student in students:
            queue.enqueue(student)
        size = len(students)

        for sandwich in sandwiches:
            count = 0
            while count < size and queue.left.value != sandwich:
                queue.enqueue(queue.dequeue())
                count += 1
            if queue.left.value != sandwich:
                return size 
            queue.dequeue()
            size -= 1
        return 0
        
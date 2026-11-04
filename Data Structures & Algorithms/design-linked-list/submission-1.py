class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    #dummy node at beginning and end
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        cur = self.left.next
        newHead = ListNode(val)
        self.left.next = newHead
        newHead.next = cur
        newHead.prev = self.left
        cur.prev = newHead

    def addAtTail(self, val: int) -> None:
        cur = self.right.prev
        newTail = ListNode(val)
        cur.next = newTail
        newTail.prev = cur
        newTail.next = self.right
        self.right.prev = newTail


    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0:
            node, next, prev = ListNode(val), cur, cur.prev
            prev.next = node
            next.prev = node
            node.next = next
            node.prev = prev


    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0:
            next, prev = cur.next, cur.prev
            next.prev = prev
            prev.next = next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
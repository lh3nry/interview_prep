# linked_pairs.py
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
     
    def setData(self,data):
        self.data = data
      
    def getData(self):
        return self.data
     
    def setNext(self,next):
        self.next = next
     
    def getNext(self):
        return self.next

class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None
        
    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head
                     
    def arrange_in_pairs(self):
        if self.head == None:
            return None
        cur = self.head
        stack = []
        while cur:
            stack.append(cur)
            cur = cur.next
        
        print([i.data for i in stack])
        
        cur = self.head
        while cur.next:
            top = stack.pop(-1)
            if cur.data == top.data or cur.next.data == top.data:
                top.next = None
                break
            print(top.data)
            # if top.next:
            top.next = None
            next_temp = cur.next
            cur.next = top
            cur.next.next = next_temp




ll = SinglyLinkedList()
h = Node(1)

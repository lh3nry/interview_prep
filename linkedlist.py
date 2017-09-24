class Node:
    def __init__(self,data):
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
    def __init__(self,head=None):
        self.head = head
        
    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head
                      
    def reverse(self):
        curr = self.head
        if curr.getNext() == None: return   # list length = 1. Nothing to be done
        if curr.getNext().getNext() == None:    # list length = 2. No need to loop
            next = curr.getNext()
            curr.setNext(None)
            next.setNext(curr)
            self.setHead(next)
            return
        prev = curr
        curr = self.head.getNext()
        next = curr.getNext()
        self.head.setNext(None)


        while(next.getNext()):
            curr.setNext(prev)  # flip the "arrow"
            # advance all the "pointers"
            prev = curr
            curr = next
            next = curr.getNext()

        curr.setNext(prev)  # penultimate flip
        next.setNext(curr)  # final flip
        self.setHead(next)      # give head

    def reverse2(self):
        prev = self.head
        curr = prev.next
        if not curr or not prev:
            return
        nxt = curr.next
        prev.next = None

        while nxt:
            # print(prev.data,curr.data,nxt.data)
            curr.next = prev

            prev = curr
            curr = nxt
            nxt = curr.next
            # print(prev.data,curr.data,nxt)
        
        curr.next = prev
        self.head = curr

    def print(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def insertHead(self,node):
        if not self.head:
            self.setHead(node)
        else:
            h = self.head
            node.next = h
            self.setHead(node)

    def insertTail(self,node):
        if not self.head:
            self.setHead(node)
            return
        curr = self.head
        while curr:
            prev = curr
            curr = curr.next

        prev.next = node

        if not self.head:
            return None
        
        

    def arrange_in_pairs(self):
        cur = self.head
        stack = []
        # iterate through list once to fill up the stack
        while cur:
            stack.append(cur)
            cur = cur.next
            
        # restart for insertions
        cur = self.head
        while cur.next:
            top = stack.pop(-1)
            # termination conditions
            if cur.data == top.data or cur.next.data == top.data:
                # first case for odd length lists
                # second case for even length lists
                top.next = None     # break a cycle
                break
            
            # do insertion
            next_temp = cur.next
            cur.next = top
            cur.next.next = next_temp
            
            # advance current pointer
            cur = next_temp



list1 = SinglyLinkedList(Node(5))
# node = list1.head
# node.next = Node(4)
# node.next.next = Node(3)
# node.next.next.next = Node(2)
# node.next.next.next.next = Node(1)
# nxt = list1.next
for i in range(4,0,-1):
    # print(i)
    list1.insertHead(Node(i))
    # nxt = new
    # nxt = new.next
list1.print()

# node = list1.head
# while node:
#     print(node.data)
#     node = node.next

# list1.reverse()
# list1.print()
# list1.reverse2()
# list1.print()

list1.arrange_in_pairs()
list1.print()


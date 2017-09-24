# pynode.py
class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)

def inOrderPrint(head):
	print head
	if head.next: #!= None:
		inOrderPrint(head.next)
	return

def revOrderPrint(head):
	if head == None: return
	revOrderPrint(head.next)
	print head

def inOrderPrintItr(head):
	while head:
		print head
		head = head.next
	return


def revList(head):
	curr = head.next
	prev = head
	if curr.next == None:
		curr.next = prev
		newHead = curr
		print curr
		return
	revList(curr)
	curr.next = prev
	newHead = curr
	print curr
	return newHead

node = Node("test")
print node
print "\n"

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

print "inOrderPrint"
inOrderPrint(node1)

print "\n"
print "revOrderPrint"
revOrderPrint(node1)


print "\n"
print "inOrderPrintItr"
inOrderPrintItr(node1)


print "\n"
print "revList"
n = revList(node1)
# inOrderPrint(n)

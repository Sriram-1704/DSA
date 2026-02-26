class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

a = Node(5)
b = Node(3)
c = Node(7)

a.next = b
b.next = c

head = a

# Traversing Linked List
def traverseLinkedList(head):
    curr = head

    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next
# traverseLinkedList(head)

# Insertion at the beginning

new_node = Node(6)
new_node.next = head
head = new_node
# traverseLinkedList(head)

# Insertion at the end

new_node1 = Node(8)
curr = head
while curr.next != None:
    curr = curr.next
curr.next = new_node1
# traverseLinkedList(head)

# Insertion at kth index

new_node2 = Node(4)
k = 2
curr = head
for i in range(k-1):
    curr = curr.next
new_node2.next = curr.next
curr.next = new_node2
# traverseLinkedList(head)

# Deletion at the beginning

head = head.next
# traverseLinkedList(head)

# Deleting the last node

curr = head
while curr.next.next != None:
    curr = curr.next

curr.next = None
# traverseLinkedList(head)

# Deletion at kth node

k = 2
curr = head

for i in range(k-1):
    curr = curr.next 

curr.next = curr.next.next
traverseLinkedList(head)






        
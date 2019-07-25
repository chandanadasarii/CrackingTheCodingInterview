from LinkedList import *

def reverseIterative(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev

inp = [1,2,3,4,5,6,7]

l = LinkedList(Node(inp[0]))
for i in range(1, len(inp)):
    l.append(Node(inp[i]))

l.display_list()
# l.head = reverseIterative(l.head)
l.reverseRecursive(l.head)
l.display_list()
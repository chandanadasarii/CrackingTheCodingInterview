from LinkedList import *

def partition(head, value):
    cur = head
    run = head

    while run:
        if run.value < value:
            cur.value, run.value = run.value, cur.value
            cur = cur.next
        run = run.next

inp = [3,5,8,5,10,2,1]

l = LinkedList(Node(inp[0]))
for i in range(1, len(inp)):
    l.append(Node(inp[i]))

l.display_list()
partition(l.head, 5)
l.display_list()
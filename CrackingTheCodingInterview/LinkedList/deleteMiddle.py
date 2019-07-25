from LinkedList import *

def deleteMiddle(head):
    fast = head
    slow = head

    while fast.next and fast.next.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next

    prev.next = slow.next


ll = LinkedList(Node(1))
ll.append(Node(2))
ll.append(Node(3))
ll.append(Node(2))
ll.append(Node(3))
ll.append(Node(4))
ll.append(Node(4))
ll.append(Node(2))
ll.display_list()
deleteMiddle(ll.head)
ll.display_list()

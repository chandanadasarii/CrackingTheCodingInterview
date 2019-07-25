from LinkedList import *

def klast(head, k):
    current = head

    for _ in range(k-1):
        if current:
            current = current.next
        else:
            return None
    
    kptr = head

    while current.next:
        current = current.next
        kptr = kptr.next

    return kptr.value


def klastRecursive(head, k):
    if head == None:
        return 0
    index = 1 + klastRecursive(head.next, k)
    if index == k:
        print(head.value)
    return index

ll = LinkedList(Node(1))
ll.append(Node(2))
ll.append(Node(3))
ll.append(Node(2))
ll.append(Node(3))
ll.append(Node(4))
ll.append(Node(2))
ll.display_list()
print(klast(ll.head, 2))
klastRecursive(ll.head, 2)

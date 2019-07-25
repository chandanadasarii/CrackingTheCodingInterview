from LinkedList import *
 
def removeDups(head):
    valueset = set()
    prev = None

    while head:
        if head.value in valueset:
            prev.next = head.next
        else:
            valueset.add(head.value)
            prev = head
        head = head.next


def removeDupsWithoutMemory(head):
    current = head

    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next


ll = LinkedList(Node(1))
ll.append(Node(2))
ll.append(Node(3))
ll.append(Node(2))
ll.append(Node(3))
ll.append(Node(2))
ll.append(Node(2))
ll.append(Node(4))
ll.append(Node(2))
ll.display_list()
# removeDups(ll.head)
removeDupsWithoutMemory(ll.head)
ll.display_list()
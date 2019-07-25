class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        current = self.head

        if self.head:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def get_position(self, position):
        current = self.head

        if self.head:
            for i in range(position-1):
                if current.next:
                    current = current.next
                else:
                    return None
        else:
            return None

        return current.value

    def insert(self, new_element, position):
        current = self.head

        if self.head:
            for i in range(position-2):
                if current.next:
                    current = current.next
                else:
                    return
        else:
            return

        new_element.next = current.next
        current.next = new_element

    def display_list(self):
        current = self.head

        while current:
            print(current.value)
            current = current.next




ll = LinkedList(Node(1))
ll.append(Node(2))
ll.append(Node(3))
print(ll.get_position(2))
print(ll.get_position(4))
ll.insert(Node(9), 2)
print(ll.display_list())
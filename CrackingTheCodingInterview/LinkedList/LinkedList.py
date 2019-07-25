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

    def delete(self, element):
        current = self.head
        prev = None

        while current:
            if current.value == element:
                prev.next = current.next
                return
            prev = current
            current = current.next


    def display_list(self):
        current = self.head

        while current:
            print(current.value, end=" ")
            current = current.next
        print()


    def reverseRecursive(self, head):
        if head.next == None:
            self.head = head
            return 
        
        self.reverseRecursive(head.next)
        head.next.next = head
        head.next = None
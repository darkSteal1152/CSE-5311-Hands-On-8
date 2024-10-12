class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, val):
        curr = self.head
        while curr is not None and curr.val != val:
            curr = curr.next
        return curr  # Returns the node or None if not found

    def insert(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def delete(self, val):
        if self.head is None:
            return

        if self.head.val == val:
            self.head = self.head.next
            return

        curr = self.head
        while curr.next is not None and curr.next.val != val:
            curr = curr.next

        if curr.next is not None:
            curr.next = curr.next.next
        else:
            print("Value not found")

    def display(self):
        curr = self.head
        if curr is None:
            return

        while curr is not None:
            print(curr.val, end=' ')
            curr = curr.next
        print()

li = LinkedList()
li.insert(1)
li.insert(4)
li.insert(16)
li.insert(9)
li.display()
li.insert(25)
li.display()
li.delete(4)
li.display()

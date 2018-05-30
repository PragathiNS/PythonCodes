class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.self.next = self.head
        self.head = temp

    def getItemByIndex(self, i):
        if i < 0:
            raise ValueError("I can't be negative : %d" % i)
        curr = self.head
        position = 0
        while curr:
            if position == i:
                return curr
            curr = curr.next
            position += 1

        raise ValueError("List has fewer than i + 1 (%d) nodes" % (i + 1))



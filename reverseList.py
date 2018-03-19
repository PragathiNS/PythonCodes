class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverseUtil(self, curr, prev):
        # if last node mark it head
        if curr.next is None:
            self.head = curr
            curr.next = prev
            return
        # save curr.next node for recursive call
        next = curr.next
        curr.next = prev
        self.reverseUtil(next, curr)

    def reverse(self):
        if self.head is None:
            return
        self.reverseUtil(self.head, None)

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next

linkedlist = LinkedList()
linkedlist.push(1)
linkedlist.push(2)
linkedlist.push(3)
linkedlist.push(4)
linkedlist.push(5)
linkedlist.push(6)
linkedlist.push(7)

print ("Before reversal")
linkedlist.printList()

linkedlist.reverse()

print ("After reversal")
linkedlist.printList()

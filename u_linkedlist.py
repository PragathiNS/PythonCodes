class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert(self, new_element, position):
        current = self.head
        count = 1
        if position > 1:
            while current and count < position:
                if count == (position - 1):
                    new_element.next = current
                    current.next = new_element
                count += 1
                current = current.next
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def get_element(self, position):
        count = 1
        current = self.head
        if position < 1:
            return None
        while current and count <= position:
            if count == position:
                return current
            current = current.next
            count += 1
        return None

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next


e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

print (ll.head.next.next.value)
print (ll.get_element(3).value)

ll.insert(e4,3)
print (ll.get_element(3).value)

ll.delete(1)
print (ll.get_element(1).value)
print (ll.get_element(2).value)
print (ll.get_element(3).value)

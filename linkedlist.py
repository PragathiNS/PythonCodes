class ListNode:
    def __init__(self, data):
        "construtor to initiate this object"
        #store data
        self.data = data
        #store reference
        self.next = None
        return
    def has_value(self, value):
        "method to compare the value with the node data"
        if self.data == value:
            return True
        else:
            return False

class SingleLinkedList:
    def __init__(self):
        "construtor to initiate this object"
        self.head = None
        self.tail = None
        return
    def add_list_item(self, item):
        "add an item at the end of the list"

        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item
        return
    def list_length(self):
        "returns the number of list items"
        count = 0
        curr_node = self.head
        while curr_node is not None:
            count += 1
            curr_node = curr_node.next
        return count
    def output_list(self):
        "outputs the list (the value of the node, actually)"
        curr_node = self.head
        while curr_node is not None:
            print (curr_node.data)
            curr_node = curr_node.next
        return
    def unordered_search(self, value):
        "search the linked list for the node that has this value"
        node_id = 0
        results = []
        curr_node = self.head
        while curr_node is not None:
            if curr_node.data == value:
                results.append(node_id)
            curr_node = curr_node.next
            node_id += 1
        return results
    def remove_list_item_by_id(self, item_id):
        "remove the list item with the item_id"
        current_id = 0
        curr_node = self.head
        prev_node = None

        while curr_node is not None:
            if current_id == item_id:
                if prev_node is not None:
                    prev_node.next = curr_node.next
                else:
                    self.head = curr_node.next
                    return 
            prev_node = curr_node
            curr_node = curr_node.next
            current_id += 1
        return 


node1 = ListNode(15)
node2 = ListNode(8.2)
node3 = ListNode("Berlin")
node4 = ListNode(15)

track = SingleLinkedList()
print ("track length: %i" % track.list_length())

for item in [node1, node2, node3, node4]:
    track.add_list_item(item)
    print ("track length: %i" % track.list_length())
    track.output_list()

print ("unordered search for 15 : %s" % track.unordered_search(15))

remove_item = track.remove_list_item_by_id(2)
print (remove_item)

print ("track length: %i" % track.list_length())
track.output_list()


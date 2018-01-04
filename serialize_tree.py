class Node:
    def __init__(self, val):
        """ Initialize a tree"""
        self.val = val
        self.left = None
        self.right = None
    
def serialize_tree(tree):
    if tree is None:
        return []
    ret_list = []
    queue = []
    queue.append(tree)
    while (len(queue) > 0):
        ret_list.append(queue[0].val)
        node = queue.pop(0)
        
        if node.left is not None:
            queue.append(node.left)
        
        if node.right is not None:
            queue.append(node.right)
        
    return ret_list
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(None)
root.left.right = Node(3)

#n = Node(None)
print (serialize_tree(root))

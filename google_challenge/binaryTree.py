class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def add_child(parent, left_value):
    parent.left = Node(left_value) 

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print (root.val)

def preOrder(root):
    if root:
        print (root.val)
        preOrder(root.left)
        preOrder(root.right)

h = int(input("Enter the height : "))
ind_list = []
for i in range(1, 2 ** h):
    ind_list.append(i)

print (ind_list)

new_li = []
def post_associate(ind_list):
    if (len(ind_list) % 2 == 1):
        root = ind_list[-1]
        new_li.append(root)
        #return (root)
    else:
        return 

    mid = int(len(ind_list) // 2)

    left_nodes = ind_list[:mid]
    #return associate(left_nodes)

    right_nodes = ind_list[mid:-1]
    return (post_associate(left_nodes), post_associate(right_nodes))

post_associate(ind_list)
print (new_li)

def in_associate(ind_list):

ind_in = [7, 3, 5, 1]
print (ind_in)

ret = []
for q in ind_in:
    if q in range(len(new_li)):
        ret.append(new_li[q])
    else:
        ret.append(-1)

print (ret)

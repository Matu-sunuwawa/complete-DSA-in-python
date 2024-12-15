class TreeNode:
    def __init__(self, coming_value):
        self.key = coming_value
        self.left = None
        self.right = None
# helper function which can convert a tuple with the structure ( left_subtree, key, right_subtree)...to solve create tree manually.
def parse_tuple(data):
    # print(data)
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        #print(node.key)
        # if node:
        #     print("root node:",node.key)
        node.left = parse_tuple(data[0]) # recursion...the function calling itself...this one is helping to shift "left"
        node.right = parse_tuple(data[2]) # recursion...the function calling itself...this one is helping to shift "right"
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
        print("This are leaves: ",node.key)
    return node

tree2 = parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))
#print(tree2.key)
# print("it should be 4:",tree2.right.left.right.key)

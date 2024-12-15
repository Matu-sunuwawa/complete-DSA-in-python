

## BINARY SEARCH TREE, TRAVERSAL AND RECURSION

BINARY TREE:
	#1. The word "binary" indicates that each "node" in the tree can have `at most 2 children` (left or right).
	#2. Nodes can have `0, 1 or 2 children`. Nodes that do not have any children are sometimes also called "leaves".
	#3. The single node at the top is called the "root" node, and it typically where operations like search, insertion etc. begin.

1. Keys and Values: Each node of the tree stores a key (a username) and a value (a User object).
2. Binary Search Tree: The left subtree of any node only contains nodes with keys that are `lexicographically` smaller than the node's key.
3. Balanced Tree: The tree is balanced i.e. it does not skew too heavily to one side or the other. The left and right subtrees of any node shouldn't differ in height/depth by more than 1 level.

## #1 first bruteforce solution....NOT binary applied

class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        
    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)
    
    def __str__(self):
        return self.__repr__()

class UserDatabase:
    def __init__(self):
        self.users = []
    
    def insert(self, user):
        i = 0
        while i < len(self.users):
            # Find the first username greater than the new user's username
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)
    
    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
    
    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email
        
    def list_all(self):
        return self.users


## HOW TO USE IT...HOW TO MANAGE IT...
- we have test case:
aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

-  We can create a new database of users by instantiating and object of the UserDatabase class.
```
database = UserDatabase()
```
```
database.insert(hemanth)
database.insert(aakash)
database.insert(siddhant)
```
```
user = database.find('siddhant')
user
```
```
database.update(User(username='siddhant', name='Siddhant U', email='siddhantu@example.com'))
```
```
user = database.find('siddhant')
user
```
```
database.list_all()
```
testing:
```
database.insert(biraj)
database.all()
```


....WHAT WE DONE SO FAR...TO RECAP...
WE CREATE SIMPLE CLASS INSIDE WE ARE "STORING A 'LIST" OF USERS 'IN SORTED ORDER' OF USERNAMES". 

Is this good enough? To get a sense how long each function might take if there are `100 million users` on the platform, we can simply run an for or while loop on 10 million numbers.
```
%%time
for i in range(100000000):
    j = i*i
```
---->>>>It takes almost 10 seconds to execute all the iterations in the above cell.



## LETS DIVE INTO BINARY TREE
QUESTION 2: Implement a binary tree using Python, and show its usage with some examples.
---pls see `simple_binary_tree.png`

# Here's a simple class representing a node within a binary tree.
```
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
```
# Here's a simple class representing a node within a binary tree.
```
node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)
```
RUN: node0
RUN: node0.key
RUN: node0.left = node1
     node0.right = node2

ALTERNATIVE
RUN: tree = node0
RUN: tree.key
RUN: tree.left.key
RUN: tree.right.key

Q# Create the following binary tree using the TreeNode class defined above.
--- `watch TreeNode.png`

# Here's an tuple representing the tree shown above:
tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))
```
# *key concept for BST
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
# helper function which can convert a tuple with the structure ( left_subtree, key, right_subtree)...to solve create tree manually.
def parse_tuple(data):
    # print(data)
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0]) # recursion...the function calling itself...that used to shift LEFT
        node.right = parse_tuple(data[2]) # recursion...the function calling itself...that used to shift RIGHT
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node
```

# TIPS: Add print statements inside parse_tuple to display the arguments for each call of the function. Does the sequence of recursive calls make sense to you?
tree2 = parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))
RUN: tree2
RUN: tree2.key
RUN: tree2.left.key, tree2.right.key
RUN: tree2.left.left.key, tree2.left.right, tree2.right.left.key, tree2.right.right.key
RUN: tree2.right.left.right.key, tree2.right.right.left.key, tree2.right.right.right.key

Q#(Exercise): 
			  Define a function tree_to_tuple that converts a binary tree into a tuple representing the same tree. 
			  E.g. tree_to_tuple converts the tree created above to the tuple ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))). Hint: Use recursion. 
			  (i love the recursion concept, python is crazy man.)

# Let's create another helper function to display all the keys in a tree-like structure for easier visualization.(OPTIONAL)
```
def display_keys(node, space='\t', level=0):
    # print(node.key if node else None, level)
    
    # If the node is empty
    if node is None:
        print(space*level + '∅')
        return   
    
    # If the node is a leaf 
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    
    # If the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left,space, level+1)
```
RUN: display_keys(tree2, '  ')


## Traversing a Binary Tree (Now we use `inorder traversa`)

Q# The following questions are frequently asked in coding interviews and assessments:
	Q#: Write a function to perform the `inorder traversal` of a binary tree.  # you can see `inorder_traversal.png`
	Q#: Write a function to perform the `preorder traversal` of a binary tree. # you can see `preorder_traversal.png`
	Q#: Write a function to perform the `postorder traversal` of a binary tree. # you can see `postorder_traversal.png`

# Here's an implementation of `inorder traversal` of a binary tree.
```
def traverse_in_order(node):
    if node is None: 
        return []
    return(traverse_in_order(node.left) + 
           [node.key] + 
           traverse_in_order(node.right))
```
tree = parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))
RUN: display_keys(tree, '  ')
RUN: traverse_in_order(tree)

# Height and Size of a Binary Tree
```
def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))
```
RUN: tree_height(tree)
```
def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)
```
RUN: tree_size(tree)


## FINAL CODE COMPILED ALL THE ABOVE FUNCTIONS....
```
class TreeNode():
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None
    
    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))
    
    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    def traverse_in_order(self):
        if self is None: 
            return []
        return (TreeNode.traverse_in_order(self.left) + 
                [self.key] + 
                TreeNode.traverse_in_order(self.right))
    
    def display_keys(self, space='\t', level=0):
        # If the node is empty
        if self is None:
            print(space*level + '∅')
            return   

        # If the node is a leaf 
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
            return

        # If the node has children
        display_keys(self.right, space, level+1)
        print(space*level + str(self.key))
        display_keys(self.left,space, level+1)    
    
    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left),  self.key, TreeNode.to_tuple(self.right)
    
    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    @staticmethod    
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node
```
RUN: tree_tuple
tree = TreeNode.parse_tuple(tree_tuple)
RUN: tree
RUN: tree.display_keys('  ')
RUN: tree.height()
RUN: tree.size()
RUN: tree.traverse_in_order()
RUN: tree.to_tuple()

# Binary Search Tree (BST)
A binary search tree or BST is a binary tree that satisfies the following conditions:
	*The left subtree of any node only contains nodes with keys less than the node's key
	*The right subtree of any node only contains nodes with keys greater than the node's key

*It follows from the above conditions that every subtree of a binary search tree must also be a binary search tree.
Q#: Write a function to check if a binary tree is a binary search tree (BST).
Q#: Write a function to find the maximum key in a binary tree.
Q#: Write a function to find the minimum key in a binary tree.
```
def remove_none(nums):
    return [x for x in nums if x is not None]

def is_bst(node):
    if node is None:
        return True, None, None
    
    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)
    
    is_bst_node = (is_bst_l and is_bst_r and 
              (max_l is None or node.key > max_l) and 
              (min_r is None or node.key < min_r))
    
    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))
    
    # print(node.key, min_key, max_key, is_bst_node)
        
    return is_bst_node, min_key, max_key
```
tree1 = TreeNode.parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
RUN: is_bst(tree1)
tree2 = TreeNode.parse_tuple((('aakash', 'biraj', 'hemanth')  , 'jadhesh', ('siddhant', 'sonaksh', 'vishal')))
RUN: is_bst(tree2)


## Storing `Key-Value` Pairs using BSTs
1. Storing Key-Value Pairs using BSTs
    - having properties `key`, `left` and `right`, we'll also store a `value` and pointer to the parent node (for easier upward traversal).
```
class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
```
# Let's try to recreate 'binary_tree.png' BST with usernames as keys and user objects as values:
RUN: tree = BSTNode(jadhesh.username, jadhesh)
RUN: tree.key, tree.value
RUN: tree.left = BSTNode(biraj.username, biraj)
	 tree.right = BSTNode(sonaksh.username, sonaksh)
RUN: tree.left.key, tree.left.value, tree.right.key, tree.right.value
RUN: display_keys(tree)  # display function is we created b4

#1. Insertion into BST
Q#: Write a function to insert a new node into a BST.
```
def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node
```
# To create the first node, we can use the insert function with None as the target tree.
RUN: tree = insert(None, jadhesh.username, jadhesh)
# The remaining nodes can now be inserted into tree.
insert(tree, biraj.username, biraj)
insert(tree, sonaksh.username, sonaksh)
insert(tree, aakash.username, aakash)
insert(tree, hemanth.username, hemanth)
insert(tree, siddhant.username, siddhant)
insert(tree, vishal.username, siddhant)

RUN: display_keys(tree)
# Note, however, that the order of insertion of nodes `change` the structure of the resulting tree.
tree2 = insert(None, aakash.username, aakash)
insert(tree2, biraj.username, biraj)
insert(tree2, hemanth.username, hemanth)
insert(tree2, jadhesh.username, jadhesh)
insert(tree2, siddhant.username, siddhant)
insert(tree2, sonaksh.username, sonaksh)
insert(tree2, vishal.username, vishal)

RUN: display_keys(tree2)
# We call it skewed/unbalanced. `skewed_or_unbalanced.png`

#2. Finding a Node in BST
Q#: Find the value associated with a given key in a BST.
```
def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)
```
RUN: node = find(tree, 'hemanth')
RUN: node.key, node.value

#3. Updating a value in a BST
Q#: Write a function to update the value associated with a given key within a BST
```
def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value
```
RUN: update(tree, 'hemanth', User('hemanth', 'Hemanth J', 'hemanthj@example.com'))
RUN: node = find(tree, 'hemanth')
	 node.value

#4. List the nodes
Q#: Write a function to retrieve all the key-values pairs stored in a BST in the sorted order of keys.
```
def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)
```
RUN: list_all(tree)


## BALANCED BINARY TREE(BBT)
Q#: Write a function to determine if a binary tree is balanced.
```
def is_balanced(node):
    if node is None:
        return True, 0
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <=1
    height = 1 + max(height_l, height_r)
    return balanced, height
```
RUN: is_balanced(tree)
output: (True, 3) -->not balanced...`skewed_or_unbalanced.png`
RUN: is_balanced(tree2)
output: (False, 7)  -->balanced

# Balanced Binary Search Trees
Q#: Write a function to create a balanced BST from a sorted list/array of key-value pairs.
```
def make_balanced_bst(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None
    
    mid = (lo + hi) // 2
    key, value = data[mid]

    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, lo, mid-1, root)
    root.right = make_balanced_bst(data, mid+1, hi, root)
    
    return root
```
data = [(user.username, user) for user in users]
RUN: data
tree = make_balanced_bst(data)
RUN: display_keys(tree)

# Balancing an Unbalanced BST
Q#: Write a function to balance an unbalanced binary search tree.
```
def balance_bst(node):
    return make_balanced_bst(list_all(node))
    
tree1 = None

for user in users:
    tree1 = insert(tree1, user.username, user)
```
RUN: display_keys(tree1)
tree2 = balance_bst(tree1)
RUN: display_keys(tree2)


## FINAL SOLUTION FOR THE PROBLEM (A Python-Friendly Treemap)

```
class TreeMap():
    def __init__(self):
        self.root = None
        
    def __setitem__(self, key, value):
        node = find(self.root, key)
        if not node:
            self.root = insert(self.root, key, value)
            self.root = balance_bst(self.root)
        else:
            update(self.root, key, value)
            
        
    def __getitem__(self, key):
        node = find(self.root, key)
        return node.value if node else None
    
    def __iter__(self):
        return (x for x in list_all(self.root))
    
    def __len__(self):
        return tree_size(self.root)
    
    def display(self):
        return display_keys(self.root)
```
# LETS TRY HERE WE GO:
RUN: users
treemap = TreeMap()
RUN: treemap.display()

treemap['aakash'] = aakash
treemap['jadhesh'] = jadhesh
treemap['sonaksh'] = sonaksh

RUN: treemap.display()
RUN: treemap['jadhesh']
RUN: len(treemap)

treemap['biraj'] = biraj
treemap['hemanth'] = hemanth
treemap['siddhant'] = siddhant
treemap['vishal'] = vishal

RUN: treemap.display()
RUN:
	```
	for key, value in treemap:
		print(key, value)
	```
RUN:
	list(treemap)

treemap['aakash'] = User(username='aakash', name='Aakash N S', email='aakashns@example.com')
RUN:
	treemap['aakash']

	
# AVL...Adelson-Velsky Landis
## Self-Balancing Binary Trees and AVL Trees
NOTE THAT: A self-balancing binary tree remains balanced after every `insertion or deletion.` 
		   Several decades of research has gone into creating self-balancing binary trees, 
		   and many approaches have been devised e.g. B-trees, Red Black Trees and AVL (Adelson-Velsky Landis) trees.


Sources:
	Explanation of the various cases: https://youtu.be/jDM6_TnYIqE?t=482
	Implementation: https://www.geeksforgeeks.org/avl-tree-set-1-insertion/



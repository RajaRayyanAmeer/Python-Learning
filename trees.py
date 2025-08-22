class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_data):
        self.root = Node(root_data)

    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

    def levelorder(self, node):
        if not node:
            return
        queue = [node]
        while queue:
            current = queue.pop(0)
            print(current.data, end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    def count_nodes(self, node):
        if not node:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def sum_nodes(self, node):
        if not node:
            return 0
        return node.data + self.sum_nodes(node.left) + self.sum_nodes(node.right)

    def find_subtree(self, node, value):
        if not node:
            return None
        if node.data == value:
            return node
        left = self.find_subtree(node.left, value)
        if left:
            return left
        return self.find_subtree(node.right, value)

bt = BinaryTree(1)
bt.root.left = Node(2)
bt.root.right = Node(3)
bt.root.left.left = Node(4)
bt.root.left.right = Node(5)
bt.root.right.left = Node(6)
bt.root.right.right = Node(7)

print("PreOrder Traversal: ", end="")
bt.preorder(bt.root)
print("\nInOrder Traversal: ", end="")
bt.inorder(bt.root)
print("\nPostOrder Traversal: ", end="")
bt.postorder(bt.root)
print("\nLevelOrder Traversal: ", end="")
bt.levelorder(bt.root)

print("\nTotal Nodes:", bt.count_nodes(bt.root))
print("Sum of Nodes:", bt.sum_nodes(bt.root))

val = 3
sub = bt.find_subtree(bt.root, val)
if sub:
    print(f"SubTree rooted at {val} found")
else:
    print(f"SubTree with value {val} not found")
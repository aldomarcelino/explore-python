from logging import RootLogger
from turtle import right


class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insertchild(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insertchild(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insertchild(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res


root = Node(2)
root.insertchild(15)
root.insertchild(45)
root.insertchild(78)
root.insertchild(3)
root.insertchild(5)
root.PrintTree()
print("-------------")
print(root.inorderTraversal(root))

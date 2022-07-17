from turtle import pensize


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    # Insert method to create nodes

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    # findval method to compare the value with nodes

    def finddata(self, value):
        if value < self.data:
            if self.left is None:
                return str(value) + " Not Found"
            return self.left.finddata(value)
        elif value > self.data:
            if self.right is None:
                return str(value) + " Not Found"
            return self.right.finddata(value)
        else:
            print(str(self.data) + " Is found")
    # Print the tree

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        elif self.right:
            self.right.PrintTree()


# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()
print(root.finddata(7))
print(root.finddata(14))

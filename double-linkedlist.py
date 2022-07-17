# double linkedlist is a collection of data can store mulitple items in s single variable with linear access
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Doubly_lingkedlist:
    def __init__(self):
        self.head = None

    # add item at begining
    def additem(self, data):
        NewNode = Node(data)
        NewNode.next = self.head
        if self.head:
            self.head.prev = NewNode
        self.head = NewNode

    # isert a data to wehere ever we intend it
    def insertitem(self, prev_node, newdata):
        if prev_node is None:
            return
        NewNode = Node(newdata)
        NewNode.next = prev_node.next
        prev_node.next = NewNode
        NewNode.prev = prev_node
        # if NewNode.next:
        #     NewNode.next.prev = NewNode
    #

    def append(self, newdata):
        NewNode = Node(newdata)
        NewNode.next = None
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = NewNode
        NewNode.prev = last
        return

    def printlist(self, node):
        while node:
            print(node.data),
            node = node.next


dllist = Doubly_lingkedlist()
dllist.additem(1)
dllist.additem(2)
dllist.additem(3)
dllist.insertitem(dllist.head.next, 13)
dllist.append(100)
dllist.printlist(dllist.head)

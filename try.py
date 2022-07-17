# linked_list
# list is collections of data that used to store multiple item in a single variable
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        newhead = self.head
        while newhead:
            print(newhead.val)
            newhead = newhead.next

    def AtBegining(self, newdata):
        NewNode = Node(newdata)

    # updatting the new nodes next val to existing node
        NewNode.next = self.head
        self.head = NewNode

    def Inbetween(self, oldmidle, newdata):
        NewNode = Node(newdata)
        NewNode.next = oldmidle.next
        oldmidle.next = NewNode


list1 = SLinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# link first Node to second node
list1.head.next = e2
# list seond node to third node
e2.next = e3

list1.AtBegining("Sun")
list1.Inbetween(list1.head.next, "Posisi-3")
list1.listprint()

# Stack first in last out
class Stack:
    def __init__(self):
        self.stack = []

    # push
    def add(self, data):
        # using list append method to add element
        # append() method appends an element to the end os the list.
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False

    def peek(self):
        return self.stack[-1]
    # POP
    # using pop method to remove element

    def remove(self):
        if len(self.stack) >= 0:
            self.stack.pop()
        else:
            print("No element in the stack")


tamp = Stack()
tamp.add("data1")
tamp.add("data2")
tamp.add("data3")
print(tamp.peek())
tamp.remove()
print(tamp.peek())

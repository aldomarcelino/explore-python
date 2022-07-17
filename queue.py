from turtle import pensize

# Queue fist in firs out


class Queue:
    def __init__(self):
        self.queue = list()

    def addqueue(self, data):
        # used insert method to add element
        if data not in self.queue:
            self.queue.insert(0, data)
            return True
        return False

    def size(self):
        return len(self.queue)

    def printqueue(self):
        print(self.queue)

    def removequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("No element in Queue")


TheQueue = Queue()
TheQueue.addqueue("data-1")
TheQueue.addqueue("data-2")
TheQueue.addqueue("data-3")
print(TheQueue.size())
print(TheQueue.printqueue())
print(TheQueue.removequeue())

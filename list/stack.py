from list.linked_list import LinkedList


class Stack(object):
    def __init__(self):
        self.list = LinkedList()

    def push(self, data):
        self.list.push(data)

    def pop(self):
        if self.list.size() == 0:
            return None
        return self.list.delete(self.list.size() - 1)

    def offer(self):
        if self.list.size() == 0:
            return None
        return self.list.get(self.list.size() - 1)

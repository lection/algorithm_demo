# -- coding:utf-8


class _Node(object):
    def __init__(self, data, next_node = None):
        self.data = data
        self.next = next_node


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.end = None
        self._size = 0

    def _index(self, index):
        if index >= self._size or index < 0:
            return None
        curr = self.head
        count = 0
        while curr:
            if count == index:
                return curr
            count += 1
            curr = curr.next

    def get(self, index):
        node = self._index(index)
        if node:
            return node.data
        return None

    def insert(self, index, data):
        if index == self._size:
            self.push(data)
            return True
        node = self._index(index)
        if not node:
            raise BaseException('index out of bounds')
        node.next = _Node(node.data, node.next)
        node.data = data
        self._size += 1
        return True

    def push(self, data):
        self._size += 1
        if not self.end:
            self.end = self.head = _Node(data)
            return True
        node = _Node(data)
        self.end.next = node
        self.end = node

    def delete(self, index):
        if index >= self._size:
            raise BaseException('index out of bounds')
        if index == 0:
            result = self.head
            self.head = self.head.next
            if self._size == 1:
                self.end = None
        else:
            node = self._index(index - 1)
            result = node.next
            if not result.next:
                self.end = node
            node.next = result.next

        self._size -= 1
        return result.data

    def size(self):
        return self._size

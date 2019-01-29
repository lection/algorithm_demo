# -- coding:utf-8


class _Node:
    def __init__(self, data):
        self.data = data
        self.children = []


class Tree(object):
    def __init__(self):
        self.root = None

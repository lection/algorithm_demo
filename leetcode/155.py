class MinStack:

    def __init__(self):
        self.list = []
        self.minList = []
        self.min = None

    def push(self, x):
        self.list.append(x)
        if self.min is None or self.min > x:
            self.min = x
        self.minList.append(self.min)

    def pop(self):
        if len(self.list) == 0:
            return None
        r = self.list.pop()
        self.minList.pop()
        if len(self.list) > 0:
            self.min = self.minList[len(self.minList)-1]
        else:
            self.min = None
        return r

    def top(self):
        if len(self.list) == 0:
            return None
        return self.list[len(self.list) - 1]

    def getMin(self):
        return self.min


class MinStack2:

    def __init__(self):
        self.list = []
        self.minList = []
        self.count = 0

    def push(self, x):
        self.list.append(x)
        if self.count == 0:
            self.minList.append(x)
        else:
            m = self.minList[self.count - 1]
            self.minList.append(m if m < x else x)
        self.count += 1

    def pop(self):
        if self.count == 0:
            return None
        self.count -= 1
        r = self.list.pop()
        self.minList.pop()
        return r

    def top(self):
        if self.count == 0:
            return None
        return self.list[self.count - 1]

    def getMin(self):
        return self.minList[self.count - 1]



def test(ms):
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    print(ms.getMin() == -3)
    ms.pop()
    print(ms.top() == 0)
    print(ms.getMin() == -2)


test(MinStack())
test(MinStack2())

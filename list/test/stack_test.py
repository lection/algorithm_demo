from list.stack import Stack

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print(stack.pop() == 4)
print(stack.pop() == 3)

stack.push(9)
stack.push(7)
print(stack.pop() == 7)
print(stack.offer() == 9)
print(stack.pop() == 9)
print(stack.pop() == 2)
print(stack.offer() == 1)
print(stack.pop() == 1)
print(not stack.pop())

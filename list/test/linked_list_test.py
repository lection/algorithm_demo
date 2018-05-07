# -- coding:utf-8 --


from list.linked_list import LinkedList

ll = LinkedList()

ll.push(1)
ll.push(2)
ll.push(3)

ll.insert(1, 9)

print(ll.size() == 4)
print(ll.get(0) == 1)
print(ll.get(1) == 9)
print(ll.get(2) == 2)
print(ll.get(3) == 3)

ll.delete(1)
ll.delete(1)
print(ll.size() == 2)
print(ll.get(0) == 1)
print(ll.get(1) == 3)

ll.insert(1, 7)
print(ll.size() == 3)
print(ll.get(0) == 1)
print(ll.get(1) == 7)
print(ll.get(2) == 3)

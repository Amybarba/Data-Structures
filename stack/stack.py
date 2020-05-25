"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


class Stack:
    def __init__(self):
        self.size = 0
        self.stack = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.stack.append(value)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.stack.pop(len(self.stack) - 1)


my_stack = Stack()
for i in range(10):
    my_stack.push(i)
print("\n")
print(my_stack.__len__())
print(my_stack.size)
my_stack.pop()

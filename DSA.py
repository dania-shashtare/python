# stack
"""
stack = []
# push
stack.append('A')
stack.append('B')
stack.append('C')
stack.append('D')
print(stack)
# pop
poped = stack.pop()
print(f"pop item is:{poped}")
print(stack)
# peek
print(stack[-1])
# is Empty
is_empty = not bool(stack)
print(is_empty)
# print size
print(len(stack))
"""

# class stack
"""
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def isEmpty(self):
        return len(self.stack) == 0

    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            return self.stack.pop()

    def size(self):
        return len(self.stack)

    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            return self.stack[-1]

    def __str__(self):
        print(self.stack)


s1 = Stack()
s1.push("A")
s1.push("B")
s1.push("C")
s1.push("D")
s1.__str__()
em = s1.isEmpty()
print(em)
poped = s1.pop()
print(poped)
ss = s1.size()
print(ss)
pe = s1.peek()
print(pe)
"""
# stack with linked list


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def isEmpty(self):
        return self.size == 0

    def stackSize(self):
        return self.size

    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        popedvalue = self.head
        self.head = self.head.next
        self.size -= 1
        return popedvalue.value

    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        return self.head.value

    def traverseAndPrint(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end=" -> ")
            currentNode = currentNode.next
        print()


myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')

print("LinkedList: ", end="")
myStack.traverseAndPrint()
print("Peek: ", myStack.peek())
print("Pop: ", myStack.pop())
print("LinkedList after Pop: ", end="")
myStack.traverseAndPrint()
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.stackSize())

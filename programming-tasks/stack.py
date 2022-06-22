class Node:
  def __init__(self, val, next) -> None:
    self.val = val
    self.next = next

class LinkedStack:
  def __init__(self) -> None:
    self.head = Node(None,None) # stack is initially empty

  def push(self, newVal) -> None:
    node = Node(newVal,None)
    node.next = self.head
    self.head = node
  
  def peek(self) -> int:
    return self.head.val
  
  def pop(self) -> int:
    if self.head.val != None:
      val = self.head.val
      self.head = self.head.next
      return val
    return -1

stack = LinkedStack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())
print(stack.pop())
print(stack.peek())
print(stack.pop())
print(stack.peek())
print(stack.pop())
print(stack.peek())
print(stack.pop())
print(stack.peek())






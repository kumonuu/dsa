from collections import deque
from stacks import Stack

class Queue:
    def __init__(self):
        self.my_list = []
    def enqueue(self,item):
        self.my_list.append(item)
    def dequeue(self):
        self.my_list.pop(0)
    def front(self):
        return self.my_list[0]
    def rear(self):
        return self.my_list[-1]

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

#print(queue.my_list)
#print(queue.front())
#print(queue.rear())

queue.dequeue()
#print(queue.my_list)

queue2 = deque()
#print(queue2)

stack1 = Stack()
stack2 = Stack()

def enqueue(item):
    stack1.push(item)
def dequeue():
    for i in range(len(stack1.my_list)):
        item = stack1.pop()
        stack2.push(item)
    stack2.pop()
    for i in range(len(stack2.my_list)):
        item = stack2.pop()
        stack1.push(item)

print(stack1.my_list)
enqueue(1)
enqueue(2)
enqueue(3)
print(stack1.my_list)
dequeue()
print(stack1.my_list)

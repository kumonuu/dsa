from queues import Queue

class Stack:
    def __init__(self):
        self.my_list = []
    def push(self,item):
        self.my_list.append(item)
    def pop(self):
        return self.my_list.pop(-1)
    def top(self):
        return self.my_list[-1]

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

queue = Queue()

def push(item):
    queue.enqueue(item)

def pop():
    return queue.my_list.pop(-1)
        
# print(stack.my_list)
# print(stack.top())

# stack.pop()
# print(stack.top())
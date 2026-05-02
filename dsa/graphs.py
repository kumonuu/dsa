from queues import Queue
from stacks import Stack

graph = {
    "A": ["B","C","D"],
    "B": ["A","D"],
    "C": ["A","D","E"],
    "D": ["A","B","C","E"],
    "E": ["C","D"],
    "F": []
}

def bfs(start):
    visited = set([])
    queue = Queue()

    queue.enqueue(start)
    visited.add(start)

    while queue.my_list:
        key = queue.dequeue()
        print(key)
        for item in graph[key]:
            if item not in visited:
                queue.enqueue(item)
            visited.add(item)

def bfs_has_path(graph,start,end):
    if start == end:
        return True

    visited = set([])
    stack = Stack()
    stack.push(start)
    visited.add(start)

    while queue.my_list:
        key = queue.dequeue()
        for item in graph[key]:
            if item == end:
                return True
            if item not in visited:
                visited.add(item)
                queue.enqueue(item)
    return False

def dfs(start):
    visited = set([])
    stack = Stack()

    stack.push(start)
    visited.add(start)

    while stack.my_list:
        key = stack.pop()
        print(key)
        for item in graph[key]:
            if item not in visited:
                stack.push(item)
            visited.add(item)

def dfs_has_path(graph,start,end):
    if start == end:
        return True
    
    visited = set([])
    stack = Stack()
    stack.push(start)
    visited.add(start)

    while stack.my_list:
        key = stack.pop()
        for item in graph[key]:
            if item == end:
                return True
            if item not in visited:
                visited.add(item)
                stack.push(item)
    return False

print(dfs_has_path(graph,"B","E"))
print(dfs_has_path(graph,"B","F"))

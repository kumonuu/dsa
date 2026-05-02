from queues import Queue

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

def has_path(graph,start,end):
    if start == end:
        return True

    visited = set([])
    queue = Queue()
    queue.enqueue(start)
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

bfs("A")

print(has_path(graph,"B","E"))
print(has_path(graph,"A","F"))
        

        
        



from queues import Queue

graph = {
    "A": ["B","C","D"],
    "B": ["A","D"],
    "C": ["A","D","E"],
    "D": ["A","B","C","E"],
    "E": ["C","D"]
}

def breadth_first(start):
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



breadth_first("A")
        

        
        



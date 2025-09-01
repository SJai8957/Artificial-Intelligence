#Write a Python Program to implement Breadth First Search Traversal.

from collections import deque

def bfs(graph, start):
    visited = set()       
    queue = deque([start])
    
    print("BFS Traversal:", end=" ")
    while queue:
        vertex = queue.popleft()
        
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    bfs(graph, 'A')

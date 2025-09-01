#Write a Python Program to implement Water Jug Problem.

from collections import deque

def water_jug_bfs(jug1, jug2, target):
    visited = set()
    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()
        if x == target or y == target:
            print(f"Reached Target: ({x}, {y})")
            return True

        if (x, y) in visited:
            continue
        visited.add((x, y))

        next_states = [
            (jug1, y),      
            (x, jug2),    
            (0, y),        
            (x, 0),         
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),  
            (x + min(y, jug1 - x), y - min(y, jug1 - x))   
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)

    print("No solution possible")
    return False

if __name__ == "__main__":
    jug1_capacity = 4
    jug2_capacity = 3
    target = 2

    water_jug_bfs(jug1_capacity, jug2_capacity, target)

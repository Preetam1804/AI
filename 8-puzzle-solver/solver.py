from puzzle import Puzzle
from collections import deque

def BFS(initial_state_board, goal_state_board):
    initial_state=Puzzle(initial_state_board)
    goal_state=Puzzle(goal_state_board)
    queue=deque([initial_state])
    visited=set()
    visited.add(tuple(map(tuple,initial_state.board)))
    while queue:
        current_state=queue.popleft()
        if current_state.board==goal_state.board:
            path=[]
            temp=current_state
            while temp.parent is not None:
                path.append(temp.action)
                temp=temp.parent
            path.reverse()
            return path
        
        for neighbor in current_state.get_neighbors():
            neighbor_tuple=tuple(map(tuple,neighbor.board))
            if neighbor_tuple not in visited:
                queue.append(neighbor)
                visited.add(neighbor_tuple)
    return None

    
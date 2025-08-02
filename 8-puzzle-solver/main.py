from solver import BFS

def main():
    start_board = [[1, 2, 3],
                   [4, 5, 6],
                   [0, 7, 8]]

    goal_board = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 0]]

    print("Start State:")
    for row in start_board:
        print(row)
    solution_path = BFS(start_board, goal_board)
    if solution_path:
        print("\nSolution Found!")
        print("Path:", solution_path)
        print("Number of moves:", len(solution_path))
    else:
        print("\nNo solution found.")
if __name__ == "__main__":
    main()
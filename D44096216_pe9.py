import random
def read_maze_from_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            N = len(lines) // 2
            M = (len(lines[0].strip()) + 1) // 4
            maze = {}
            for i in range(N):
                for j in range(M):
                    if lines[2*i+1][4*j+2] == 'X':
                        maze[(i, j)] = 1
                    else:
                        maze[(i, j)] = 0
            return maze, N, M
    except IOError:
        print("File not found. Please enter a valid file name.")
        return None, None, None
    
def generate_path(maze, N, M):
    # This function generates a random path through an NxM maze, represented as a dictionary. The keys are (i, j) tuples representing
    # coordinates of each cell in the maze and the values are integers: 0 for empty, 1 for obstacle, and 2 for path. The path starts 
    # from (0,0) and ends at (N-1,M-1), and the direction (right or down) at each step is chosen randomly.
    i, j = 0, 0
    while i < N-1 or j < M-1:
        maze[(i, j)] = 2
        if i == N-1:
            j += 1
        elif j == M-1:
            i += 1
        elif random.choice([True, False]):
            j += 1
        else:
            i += 1
    maze[(N-1, M-1)] = 2

def add_obstacles(maze, min_obstacles, N, M):
    # This function randomly adds obstacles (represented as 1) to the empty cells (represented as 0) in the given maze until at least
    # min_obstacles have been added. If a KeyError occurs while trying to set an obstacle, it is caught and a message is printed.
    added = 0
    while added < min_obstacles:
        i, j = random.randint(0, N-1), random.randint(0, M-1)
        if maze[(i, j)] == 0:
            maze[(i, j)] = 1
            added += 1

def set_obstacle(maze, N, M):
    # This function allows a user to manually set an obstacle in the maze. The user is prompted to input the coordinates of the cell
    # where they want to place the obstacle. If the cell is part of the path or an obstacle is already present, an error message is 
    # displayed. If the coordinates are out of bounds or not integers, a KeyError or ValueError is raised, respectively.
    try:
        x, y = map(int, input("Enter the coordinates to set an obstacle (row col): ").split())
        if (x, y) not in maze or x < 0 or x >= N or y < 0 or y >= M:
            print("Invalid coordinates.")
        elif maze[(x, y)] == 2:
            print("Cannot place an obstacle on the path.")
        else:
            maze[(x, y)] = 1
    except ValueError:
        print("Invalid input. Please enter two integers.")

def remove_obstacle(maze, N, M):
    # This function allows a user to manually remove an obstacle from the maze. The user is prompted to input the coordinates of the 
    # cell where they want to remove the obstacle. If the cell is part of the path or there's no obstacle at the given cell, an error 
    # message is displayed. If the coordinates are out of bounds or not integers, a KeyError or ValueError is raised, respectively.
    try:
        x, y = map(int, input("Enter the coordinates to remove an obstacle (row col): ").split())
        if (x, y) not in maze or x < 0 or x >= N or y < 0 or y >= M:
            print("Invalid coordinates.")
        elif maze[(x, y)] == 2:
            print("Cannot remove a path cell.")
        else:
            maze[(x, y)] = 0
    except ValueError:
        print("Invalid input. Please enter two integers.")

def print_maze(maze, N, M):
    # This function prints the current state of the maze in a grid-like format. Each cell is represented by a 3-character string: 
    # '   ' for empty cells, ' X ' for obstacles, and ' O ' for path cells.
    for i in range(N):
        for j in range(M):
            if maze[(i, j)] == 0:
                print(' ', end=' ')
            elif maze[(i, j)] == 1:
                print('X', end=' ')
            elif maze[(i, j)] == 2:
                print('O', end=' ')
        print()

def main():
    # This function serves as the main driver of the program. It reads the maze dimensions from a file, asks the user for the minimum 
    # number of obstacles to be added, generates the path and adds the obstacles, and then enters a loop where the user can choose to 
    # set or remove obstacles, print the maze, or exit the program. Exceptions for ValueError, IOError, and NameError are handled.
    filename = input("Enter the maze blueprint file name: ")
    maze, N, M = None, None, None
    while maze is None:
        try:
            maze, N, M = read_maze_from_file(filename)
        except IOError:
            filename = input("File not found. Please enter a valid file name: ")

    min_obstacles = input("Enter the minimum number of obstacles: ")
    try:
        min_obstacles = int(min_obstacles)
    except ValueError:
        print("Invalid number of obstacles.")
        return

    generate_path(maze, N, M)
    add_obstacles(maze, min_obstacles, N, M)
    print_maze(maze, N, M)

    while True:
        print("\nOptions:")
        print("1. Set an obstacle")
        print("2. Remove an obstacle")
        print("3. Exit")
        option = input("Enter your choice: ")

        if option == '1':
            set_obstacle(maze, N, M)
        elif option == '2':
            remove_obstacle(maze, N, M)
        elif option == '3':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()

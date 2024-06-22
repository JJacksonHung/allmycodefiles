import curses
import random

# Constants
NORMAL_FOOD = 'π'
SPECIAL_FOOD = 'X'
OBSTACLE = '#'
SNAKE_BODY = 'O'
SNAKE_HEAD = '@'
INITIAL_SNAKE_LENGTH = 3
INITIAL_DIRECTION = curses.KEY_RIGHT

# Function to initialize the game screen and set up initial variables
def initialize_screen():
    screen = curses.initscr()
    curses.curs_set(0)
    screen.timeout(100)
    screen.keypad(1)
    screen_height, screen_width = screen.getmaxyx()
    return screen, screen_height, screen_width

# Function to place the snake on the screen
def place_snake(screen, snake):
    for segment in snake:
        screen.addch(segment[0], segment[1], SNAKE_BODY)
    screen.addch(snake[0][0], snake[0][1], SNAKE_HEAD)

# Function to generate random positions for food and obstacles
def generate_food(screen, snake, obstacles, screen_height, screen_width):
    while True:
        food_position = (random.randint(1, screen_height - 2), random.randint(1, screen_width - 2))
        if food_position not in snake and food_position not in obstacles:
            return food_position

def generate_obstacles(screen, screen_height, screen_width):
    obstacles = set()
    num_obstacles = int(screen_height * screen_width * 0.05 / 5)
    for _ in range(num_obstacles):
        orientation = random.choice(['horizontal', 'vertical'])
        if orientation == 'horizontal':
            start_row = random.randint(1, screen_height - 2)
            start_col = random.randint(1, screen_width - 7)
            for i in range(5):
                obstacles.add((start_row, start_col + i))
        else:
            start_row = random.randint(1, screen_height - 7)
            start_col = random.randint(1, screen_width - 2)
            for i in range(5):
                obstacles.add((start_row + i, start_col))
    return obstacles

# Main function to run the game
def main(screen):
    screen, screen_height, screen_width = initialize_screen()
    snake = [(screen_height // 2, screen_width // 2 - i) for i in range(INITIAL_SNAKE_LENGTH)]
    direction = INITIAL_DIRECTION
    paused = False
    normal_food_count = 0
    special_food_count = 0
    normal_food_pos = generate_food(screen, snake, [], screen_height, screen_width)
    special_food_pos = generate_food(screen, snake, [], screen_height, screen_width)
    obstacles = generate_obstacles(screen, screen_height, screen_width)

    for obstacle in obstacles:
        screen.addch(obstacle[0], obstacle[1], OBSTACLE)

    place_snake(screen, snake)

    while True:
        key = screen.getch()

        if key == ord(' '):
            paused = not paused
        elif key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            if (key == curses.KEY_RIGHT and direction != curses.KEY_LEFT) or \
               (key == curses.KEY_LEFT and direction != curses.KEY_RIGHT) or \
               (key == curses.KEY_UP and direction != curses.KEY_DOWN) or \
               (key == curses.KEY_DOWN and direction != curses.KEY_UP):
                direction = key

        if paused:
            continue

        head = snake[0]
        new_head = (head[0], head[1])

        if direction == curses.KEY_RIGHT:
            new_head = (head[0], (head[1] + 1) % screen_width)
        elif direction == curses.KEY_LEFT:
            new_head = (head[0], (head[1] - 1) % screen_width)
        elif direction == curses.KEY_UP:
            new_head = ((head[0] - 1) % screen_height, head[1])
        elif direction == curses.KEY_DOWN:
            new_head = ((head[0] + 1) % screen_height, head[1])

        if new_head in snake or new_head in obstacles:
            break

        snake.insert(0, new_head)

        if new_head == normal_food_pos:
            normal_food_count += 1
            normal_food_pos = generate_food(screen, snake, obstacles, screen_height, screen_width)
        elif new_head == special_food_pos:
            special_food_count += 1
            special_food_pos = generate_food(screen, snake, obstacles, screen_height, screen_width)
            if len(snake) > 1:
                snake.pop()
        else:
            snake.pop()

        screen.clear()
        for y, x in snake:
            screen.addch(y, x, SNAKE_BODY)
        screen.addch(snake[0][0], snake[0][1], SNAKE_HEAD)
        screen.addch(normal_food_pos[0], normal_food_pos[1], NORMAL_FOOD)
        screen.addch(special_food_pos[0], special_food_pos[1], SPECIAL_FOOD)

        for obstacle in obstacles:
            screen.addch(obstacle[0], obstacle[1], OBSTACLE)

        screen.refresh()

    curses.endwin()
    print(f"Game Over! You ate {normal_food_count} normal foods and {special_food_count} special foods.")

if __name__ == "__main__":
    curses.wrapper(main)

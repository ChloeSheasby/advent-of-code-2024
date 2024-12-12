from aocd import get_data


# stack to keep track of path
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x, y):
        self.stack.append((x, y))

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        return self.stack[-1]


def read_puzzle_input_to_nested_array():
    data = get_data(day=6, year=2024)

    map = []

    for line in data.split("\n"):
        temp = []
        for char in line:
            temp.append(char)
        map.append(temp)

    return map


def find_next_move(map, x, y, dir):
    directions = {
        "up": (0, -1, "right"),
        "right": (1, 0, "down"),
        "down": (0, 1, "left"),
        "left": (-1, 0, "up")
    }

    dx, dy, new_dir = directions[dir]

    if 0 <= y + dy < len(map) and 0 <= x + dx < len(map[0]) and map[y + dy][x + dx] != "#" and map[y + dy][x + dx] != "0":
        return x + dx, y + dy, dir

    return x, y, new_dir


def run_maze(map, x, y, dir):
    path = []
    while y >= 0 and x >= 0 and y < len(map) - 1 and x < len(map[y]) - 1:
        x, y, dir = find_next_move(map, x, y, dir)
        map[y][x] = "X"


def part_a(map):
    for i, row in enumerate(map):
        for j, char in enumerate(row):
            if char == "^":
                x = j
                y = i
                break

    map[y][x] = "X"

    dir = "up"

    run_maze(map, x, y, dir)

    count = 0
    for row in map:
        count += row.count("X")

    return count


def part_b(map):
    loop_count = 0
    for i, row in enumerate(map):
        for j, char in enumerate(row):
            if char == ".":
                # make a copy of the map
                temp_map = map.copy()
                temp_map[i][j] = "0"
                # run map and see if it gets into a loop
                path = []


    return loop_count


def main():
    temp = read_puzzle_input_to_nested_array()
    answer1 = part_a(temp)
    print(f"The number of distinct positions visited is {answer1}")
    answer2 = part_b(temp)
    print(f"The number of loops that can be created is {answer2}")


if __name__ == "__main__":
    main()

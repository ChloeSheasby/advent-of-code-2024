import copy

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


def find_next_move(map, x, y, dir, double=False):
    directions = {
        "up": (0, -1, "right"),
        "right": (1, 0, "down"),
        "down": (0, 1, "left"),
        "left": (-1, 0, "up")
    }

    dx, dy, new_dir = directions[dir]

    if 0 > y + dy or y + dy >= len(map) or 0 > x + dx or x + dx >= len(map[0]):
        return x + dx, y + dy, dir

    if map[y + dy][x + dx] != "#" and map[y + dy][x + dx] != "0":
        map[y + dy][x + dx] = "X"
        if double:
            return find_next_move(map, x + dx, y + dy, dir)
        return x + dx, y + dy, dir

    return find_next_move(map, x, y, new_dir, double)


def find_starting_point(map):
    for i, row in enumerate(map):
        for j, char in enumerate(row):
            if char == "^":
                return j, i


def run_maze(map, x, y, dir):
    while y >= 0 and x >= 0 and y < len(map) - 1 and x < len(map[y]) - 1:
        x, y, dir = find_next_move(map, x, y, dir)


def run_maze_with_two_steppers(map, x1, y1, x2, y2, dir1, dir2):
    while y2 >= 0 and x2 >= 0 and y2 < len(map) - 1 and x2 < len(map[y2]) - 1:
        x1, y1, dir1 = find_next_move(map, x1, y1, dir1)
        x2, y2, dir2 = find_next_move(map, x2, y2, dir2, True)
        if x1 == x2 and y1 == y2 and dir1 == dir2:
            return True
        
    return False


def part_a(map):
    x, y = find_starting_point(map)

    map[y][x] = "X"

    dir = "up"

    run_maze(map, x, y, dir)

    count = 0
    for row in map:
        count += row.count("X")

    return count


def part_b(map):
    x, y = find_starting_point(map)

    map[y][x] = "X"

    loop_count = 0
    for i, row in enumerate(map):
        for j, char in enumerate(row):
            if char == ".":
                # make a copy of the map
                temp_map = copy.deepcopy(map)
                temp_map[i][j] = "0"
                # run map and see if it gets into a loop
                temp = run_maze_with_two_steppers(
                    temp_map, x, y, x, y, "up", "up"
                )
                if temp:
                    loop_count += 1

    return loop_count


def main():
    temp = read_puzzle_input_to_nested_array()
    print(temp)
    answer1 = part_a(copy.deepcopy(temp))
    print(f"The number of distinct positions visited is {answer1}")
    answer2 = part_b(copy.deepcopy(temp))
    print(f"The number of loops that can be created is {answer2}")


if __name__ == "__main__":
    main()

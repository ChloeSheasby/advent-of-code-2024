from aocd import get_data


def read_puzzle_input_to_nested_array():
    data = get_data(day=7, year=2024)

    equations = {}

    for line in data.split("\n"):
        temp = line.split(":")
        temp2 = []
        for char in temp[1]:
            temp.append(char)
        equations[temp[0]] = temp2

    return equations


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


def main():
    temp = read_puzzle_input_to_nested_array()
    print(temp)
    answer1 = part_a(temp)
    print(f"The number of distinct positions visited is {answer1}")


if __name__ == "__main__":
    main()

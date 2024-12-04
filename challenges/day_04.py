from aocd import get_data


def read_puzzle_input_to_nested_array():
    data = get_data(day=4, year=2024)

    temp = []
    for line in data.split("\n"):
        temp.append(list(line))

    return temp


def check_for_xmas(array, i, j, directions):
    x, y = directions

    try:
        mx, my = j + y, i + x
        ax, ay = j + 2 * y, i + 2 * x
        sx, sy = j + 3 * y, i + 3 * x

        if (mx < 0 or ax < 0 or sx < 0 or
                my < 0 or ay < 0 or sy < 0):
            return False

        xmas = (array[j][i] +
                array[mx][my] +
                array[ax][ay] +
                array[sx][sy])

        return xmas == "XMAS"
    except IndexError:
        return False


def check_for_x_mas(array, i, j, direction_pair):
    x1, y1 = direction_pair[0]
    x2, y2 = direction_pair[1]

    try:
        if (j + y1 < 0 or i + x1 < 0 or
                j + y2 < 0 or i + x2 < 0):
            return False

        ms = (array[j + y1][i + x1] +
              array[j + y2][i + x2])

        return ms in ("MS", "SM")
    except IndexError:
        return False


def part_a(array):
    xmas_count = 0

    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1)
    ]

    for j, line in enumerate(array):
        for i, character in enumerate(line):
            if character == "X":
                for direction in directions:
                    if check_for_xmas(array, i, j, direction):
                        xmas_count += 1

    return xmas_count


def part_b(array):
    x_mas_count = 0

    direction_pairs = [
        [(1, -1), (-1, 1)],
        [(1, 1), (-1, -1)]
    ]

    for j, line in enumerate(array):
        for i, character in enumerate(line):
            if character == "A":
                if (check_for_x_mas(array, i, j, direction_pairs[0]) and
                        check_for_x_mas(array, i, j, direction_pairs[1])):
                    x_mas_count += 1

    return x_mas_count


def main():
    array1 = read_puzzle_input_to_nested_array()
    answer1 = part_a(array1)
    print(f"The number of xmas is: {answer1}")
    answer2 = part_b(array1)
    print(f"The number of x_mas is: {answer2}")


if __name__ == "__main__":
    main()

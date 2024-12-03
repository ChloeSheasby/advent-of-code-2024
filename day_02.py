from aocd import get_data


def read_puzzle_input_to_nested_array():
    data = get_data(day=2, year=2024)

    temp = []
    for line in data.split("\n"):
        temp.append([int(x) for x in line.split()])

    return temp


def check_safety(array):
    is_increasing = True
    is_decreasing = True
    is_within_range = True

    for i in range(len(array) - 1):
        if abs(array[i + 1] - array[i]) > 3:
            is_within_range = False
            break
        if array[i] >= array[i + 1]:
            is_increasing = False
        if array[i] <= array[i + 1]:
            is_decreasing = False

    return is_within_range and (is_increasing or is_decreasing)


def part_a(array):
    total_safe = 0
    for value in array:
        if check_safety(value):
            total_safe += 1

    return total_safe


def part_b(array):
    total_safe = 0
    for value in array:
        for i in range(len(value)):
            temp = value.copy()
            temp.pop(i)
            if check_safety(temp):
                value = temp
                break

        if check_safety(value):
            total_safe += 1

    return total_safe


def main():
    array1 = read_puzzle_input_to_nested_array()
    answer1 = part_a(array1)
    print(f"The number of safe reports is: {answer1}")
    answer2 = part_b(array1)
    print(f"The new number of safe reports is: {answer2}")


if __name__ == "__main__":
    main()

from aocd import get_data


def read_puzzle_input_to_dictionary():
    data = get_data(day=7, year=2024)

    equations = {}

    for line in data.split("\n"):
        temp = line.split(":")
        values = [int(x) for x in temp[1].strip().split()]
        equations[temp[0]] = values

    return equations


def is_solvable(expected, values, current_value, index):
    if index == len(values):
        return current_value == expected

    return (is_solvable(expected, values, current_value + int(values[index]),
                        index + 1) or
            is_solvable(expected, values, current_value * int(values[index]),
                        index + 1))


def is_solvable_part_b(expected, values, current_value, index):
    if index == len(values):
        return current_value == expected

    return (is_solvable_part_b(expected, values, 
                               current_value + int(values[index]), 
                               index + 1) or
            is_solvable_part_b(expected, values, 
                               current_value * int(values[index]), 
                               index + 1) or
            is_solvable_part_b(expected, values, 
                               int(f"{current_value}{values[index]}"), 
                               index + 1))


def part_a(data):
    sum_of_test_values = 0
    for line in data.split("\n"):
        parts = line.strip().split(":")
        key = int(parts[0])
        values = [int(x) for x in parts[1].strip().split()]
        print(key, values)
        if is_solvable(key, values, values[0], 1):
            sum_of_test_values += key

    return sum_of_test_values


def part_b(data):
    sum_of_test_values = 0
    for line in data.split("\n"):
        parts = line.strip().split(":")
        key = int(parts[0])
        values = [int(x) for x in parts[1].strip().split()]
        print(key, values)
        if is_solvable_part_b(key, values, values[0], 1):
            sum_of_test_values += key

    return sum_of_test_values


def main():
    data = get_data(day=7, year=2024)
    answer1 = part_a(data)
    print(f"The total calibration result is {answer1}")
    answer2 = part_b(data)
    print(f"The new total calibration result is {answer2}")


if __name__ == "__main__":
    main()

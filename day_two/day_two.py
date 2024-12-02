def read_puzzle_input_to_nested_array():
    with open("../day_two/puzzle_input.txt", encoding="utf-8") as file:
        lines = file.readlines()

    temp = []
    for line in lines:
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


def calculate_safety(array):
    total_safe = 0
    for value in array:
        if check_safety(value):
            total_safe += 1

    return total_safe


def calculate_possible_safety(array):
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


array1 = read_puzzle_input_to_nested_array()
answer1 = calculate_safety(array1)
print(answer1)
answer2 = calculate_possible_safety(array1)
print(answer2)

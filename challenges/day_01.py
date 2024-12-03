from aocd import get_data


def read_puzzle_input_to_arrays():
    data = get_data(day=1, year=2024)

    temp1 = []
    temp2 = []
    for line in data.split("\n"):
        x, y = line.split()
        temp1.append(int(x))
        temp2.append(int(y))

    return temp1, temp2


def part_a(array1, array2):
    array1.sort()
    array2.sort()

    distance = 0
    for i, value in enumerate(array1):
        distance += abs(array2[i] - value)

    return distance


def part_b(array1, array2):
    similarity = 0
    for value in array1:
        temp = array2.count(value)
        similarity += temp * value

    return similarity


def main():
    array1, array2 = read_puzzle_input_to_arrays()
    answer1 = part_a(array1, array2)
    print(f"The distance is: {answer1}")
    answer2 = part_b(array1, array2)
    print(f"The similarity is: {answer2}")


if __name__ == "__main__":
    main()

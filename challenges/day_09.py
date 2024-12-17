
from aocd import get_data


def read_puzzle_input_to_dict():
    data = get_data(day=9, year=2024)

    temp = list(data)
    files = []
    space = []

    for i, value in enumerate(temp):
        if i % 2 == 0:
            files.append(int(value))
        else:
            space.append(int(value))

    return files, space


def create_list_from_files_and_space(files, space):
    temp_string = []
    index = 0

    for i, file_count in enumerate(files):
        temp_string.extend([index] * file_count)
        if i < len(space):
            temp_string.extend(["."] * space[i])
        index += 1

    return temp_string


def organize_string(temp_string):
    for i, char in enumerate(temp_string):
        if char == ".":
            for j in range(len(temp_string) - 1, i, -1):
                if temp_string[j] != ".":
                    temp_string[i], temp_string[j] = (
                        temp_string[j], temp_string[i]
                    )
                    break

    return temp_string


def organize_string_by_chunks(temp_string, files):
    for i in range(len(temp_string) - 1, 0, -1):
        if temp_string[i] != ".":
            size_for_files = files[temp_string[i]]
            test_size_for_files = 0
            for j in range(0, i):
                if test_size_for_files == size_for_files:
                    temp_string[i - size_for_files + 1: i + 1], temp_string[j - size_for_files: j] = (
                        temp_string[j - size_for_files: j],
                        temp_string[i - size_for_files + 1: i + 1]
                    )
                    i -= size_for_files
                    break

                if temp_string[j] == ".":
                    test_size_for_files += 1
                else:
                    test_size_for_files = 0

    print(temp_string)

    return temp_string


def part_a(files, space):
    initial_list = create_list_from_files_and_space(files, space)
    ordered_list = organize_string(initial_list)

    result = 0
    for i, value in enumerate(ordered_list):
        if value != ".":
            result += i * int(value)

    return result


def part_b(files, space):
    initial_list = create_list_from_files_and_space(files, space)
    ordered_list = organize_string_by_chunks(initial_list, files)

    result = 0
    for i, value in enumerate(ordered_list):
        if value != ".":
            result += i * int(value)

    return result


def main():
    files, space = read_puzzle_input_to_dict()
    print(files, space)
    answer1 = part_a(files, space)
    print(f"The resulting filesystem checksum is {answer1}")
    answer2 = part_b(files, space)
    print(f"The resulting filesystem checksum is {answer2}")


if __name__ == "__main__":
    main()

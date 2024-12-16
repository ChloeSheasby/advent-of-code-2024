import copy

from aocd import get_data


def read_puzzle_input_to_map():
    data = get_data(day=8, year=2024)

    map = []

    for line in data.split("\n"):
        temp = []
        for char in line:
            temp.append(char)
        map.append(temp)

    return map


def part_a(map):
    total_anti_nodes = set()

    char_dict = {}
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if map[y][x] != ".":
                if map[y][x] not in char_dict:
                    char_dict[map[y][x]] = []
                char_dict[map[y][x]].append((x, y))

    for _, points in char_dict.items():
        for i, point_i in enumerate(points):
            for j, point_j in enumerate(points):
                if i == j:
                    continue
                distance = (points[i][0] - points[j][0],
                            points[i][1] - points[j][1])
                y_pos_index = points[i][1] + distance[1]
                x_pos_index = points[i][0] + distance[0]
                y_neg_index = points[j][1] - distance[1]
                x_neg_index = points[j][0] - distance[0]
                if (0 <= y_pos_index < len(map) and
                        0 <= x_pos_index < len(map[0])):
                    total_anti_nodes.add((y_pos_index, x_pos_index))
                if (0 <= y_neg_index < len(map) and
                        0 <= x_neg_index < len(map[0])):
                    total_anti_nodes.add((y_neg_index, x_neg_index))

    return len(set(total_anti_nodes))


def part_b(map):
    total_anti_nodes = set()

    char_dict = {}
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if cell != ".":
                if map[y][x] not in char_dict:
                    char_dict[map[y][x]] = []
                char_dict[map[y][x]].append((y, x))

    for _, points in char_dict.items():
        for i, point_i in enumerate(points):
            for j, point_j in enumerate(points):
                if i == j:
                    continue

                if len(points) > 1:
                    total_anti_nodes.add(point_i)

                distance = (point_i[0] - point_j[0],
                            point_i[1] - point_j[1])
                
                y_pos_index = point_i[0] + distance[0]
                x_pos_index = point_i[1] + distance[1]
                y_neg_index = point_i[0] - distance[0]
                x_neg_index = point_i[1] - distance[1]

                while (0 <= y_pos_index < len(map) and
                        0 <= x_pos_index < len(map[0])):
                    if map[y_pos_index][x_pos_index] == ".":
                        total_anti_nodes.add((y_pos_index, x_pos_index))
                    y_pos_index += distance[0]
                    x_pos_index += distance[1]

                while (0 <= y_neg_index < len(map) and
                        0 <= x_neg_index < len(map[0])):
                    if map[y_neg_index][x_neg_index] == ".":
                        total_anti_nodes.add((y_neg_index, x_neg_index))
                    y_neg_index -= distance[0]
                    x_neg_index -= distance[1]

    return len(set(total_anti_nodes))


def main():
    map_array = read_puzzle_input_to_map()
    print(map_array)
    answer1 = part_a(copy.deepcopy(map_array))
    print(f"The total unique locations of anti-nodes is {answer1}")
    answer2 = part_b(copy.deepcopy(map_array))
    print(f"The total unique locations of anti-nodes considering "
          f"resonant harmonics is {answer2}")


if __name__ == "__main__":
    main()


import networkx as nx
import numpy as np
from aocd import get_data


def read_puzzle_input_to_map():
    data = get_data(day=10, year=2024)

    topographic_map = []

    for line in data.split("\n"):
        temp = []
        for char in line:
            temp.append(char)
        topographic_map.append(temp)

    return topographic_map


def array_to_graph(topographic_map):
    adj_matrix = np.array(topographic_map)
    graph = nx.from_numpy_matrix(adj_matrix)

    return graph


def breadth_first_search(graph, start, end):
    queue = [(start, [start])]
    while queue:
        (node, path) = queue.pop(0)
        for next in graph[node]:
            if next == end:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

    return None


def find_starting_positions(topographic_map):
    starting_positions = []
    for y, row in enumerate(topographic_map):
        for x, cell in enumerate(row):
            if topographic_map[y][x] == '0':
                starting_positions.append((x, y))

    return starting_positions


def find_ending_positions(topographic_map):
    ending_positions = []
    for y, row in enumerate(topographic_map):
        for x, cell in enumerate(row):
            if topographic_map[y][x] == '9':
                ending_positions.append((x, y))

    return ending_positions


def find_next_move(topographic_map, x, y, current_index):
    possible_moves = []

    if y - 1 >= 0 and topographic_map[y - 1][x] == str(current_index + 1):
        possible_moves.append((x, y - 1, current_index + 1))
    
    if x + 1 < len(topographic_map[y]) and topographic_map[y][x + 1] == str(current_index + 1):
        possible_moves.append((x + 1, y, current_index + 1))
    
    if y + 1 < len(topographic_map) and topographic_map[y + 1][x] == str(current_index + 1):
        possible_moves.append((x, y + 1, current_index + 1))
    
    if x - 1 >= 0 and topographic_map[y][x - 1] == str(current_index + 1):
        possible_moves.append((x - 1, y, current_index + 1))
    
    return possible_moves


def run_trail(topographic_map, x, y, fx, fy):
    def temp(x, y, current_index):
        if x == fx and y == fy and current_index == 9:
            return 1
        
        possible_moves = find_next_move(topographic_map, x, y, current_index)
        for move in possible_moves:
            x, y, current_index = move
            if temp(x, y, current_index):
                return 1
        
        return 0
    
    return temp(x, y, 0)


def part_a(topo_map):
    total_trailhead_score = 0

    starting_positions = find_starting_positions(topo_map)
    ending_positions = find_ending_positions(topo_map)

    for starting_position in starting_positions:
        x, y = starting_position
        for ending_position in ending_positions:
            fx, fy = ending_position
            # can we reach the ending position from the starting position?
            total_trailhead_score += run_trail(topo_map, x, y, fx, fy)

    return total_trailhead_score


def part_b(topo_map):
    total_unique_paths = 0
    graph = array_to_graph(topo_map)

    starting_positions = find_starting_positions(topo_map)
    ending_positions = find_ending_positions(topo_map)

    for starting_position in starting_positions:
        x, y = starting_position
        for ending_position in ending_positions:
            fx, fy = ending_position
            paths = breadth_first_search(graph, (x, y), (fx, fy))
            total_unique_paths += len(list(paths))

    return total_unique_paths


def main():
    topo_map = read_puzzle_input_to_map()
    print(topo_map)
    answer1 = part_a(topo_map)
    print(f"The total trailhead score is is {answer1}")
    answer2 = part_b(topo_map)
    print(f"The total number of unique paths is {answer2}")


if __name__ == "__main__":
    main()

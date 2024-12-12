from itertools import product
from typing import Callable

from aocd import get_data

operators = [
    lambda a, b: a + b,
    lambda a, b: a * b,
    # lambda a, b: int(f"{a}{b}") # comment out for pt 1
]


def evaluate(operands: [int], ops:[Callable[[int,int],int]]) -> int:
    result = operands[0]
    for i in range(len(ops)):
        result = ops[i](result, operands[i+1])
    return result


def is_valid(test_val: int, operands: [int]) -> bool:
    operator_combos = product(operators, repeat=len(operands) - 1)
    for operator_combo in operator_combos:
        if evaluate(operands, operator_combo) == test_val:
            return True
    return False


def test(data):
    answer = 0
    for key, values in data.items():
        print(key, values)
        if is_valid(key, values):
            answer += key
    for line in data.split("\n"):
        print(line)
        parts = line.strip().split(":")
        test_val = int(parts[0])
        operands = [int(x) for x in parts[1].strip().split()]
        if is_valid(test_val, operands):
            answer += test_val

    return answer


def read_puzzle_input_to_dictionary():
    data = get_data(day=7, year=2024)

    equations = {}

    for line in data.split("\n"):
        print(line)
        parts = line.strip().split(":")
        test_val = int(parts[0])
        operands = [int(x) for x in parts[1].split()]
        equations[test_val] = operands
        print(equations[test_val])

    return equations


def main():
    temp = read_puzzle_input_to_dictionary()
    # print(temp)
    answer = test(temp)
    print(f"answer is {answer}")


if __name__ == '__main__':
    main()

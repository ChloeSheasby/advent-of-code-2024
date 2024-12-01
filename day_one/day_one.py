def read_puzzle_input_to_arrays():
    with open("../day_one/puzzle_input.txt", encoding="utf-8") as file:
        lines = file.readlines()
    
    temp1 = []
    temp2 = []
    for line in lines:
        x, y = line.split()
        temp1.append(int(x))
        temp2.append(int(y))

    return temp1, temp2


def calculate_distance(array1, array2):
    array1.sort()
    array2.sort()

    distance = 0
    for i, value in enumerate(array1):
        distance += abs(array2[i] - value)

    return distance


def calculate_similarity(array1, array2):
    similarity = 0
    for i, value in enumerate(array1):
        # count the number of times value is in array2
        temp = array2.count(value)
        similarity += temp * value

    return similarity


array1, array2 = read_puzzle_input_to_arrays()
answer1 = calculate_distance(array1, array2)
print(answer1)
answer2 = calculate_similarity(array1, array2)
print(answer2)

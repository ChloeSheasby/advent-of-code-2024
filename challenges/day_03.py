from aocd import get_data


class Lexer:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def next(self):
        if self.index >= len(self.data):
            return "end"

        character = self.data[self.index]
        self.index += 1

        if character == 'd':
            if self.data[self.index-1:self.index+6] == "don't()":
                self.index += 6
                return "dont"

            if self.data[self.index-1:self.index+3] == "do()":
                self.index += 3
                return "do"

        if character == 'm' and self.data[self.index-1:self.index+2] == 'mul':
            self.index += 2
            return "mul"

        if character.isdigit():
            num = character
            while self.data[self.index].isdigit():
                num += self.data[self.index]
                self.index += 1
            return int(num)

        if (character == '(' and self.data[self.index-2] == 'l' and
                self.data[self.index].isdigit()):
            return '('

        if character == ')' and self.data[self.index-2].isdigit():
            return ')'

        if (character == ',' and self.data[self.index-2].isdigit() and
                self.data[self.index].isdigit()):
            return ','

        return None


def get_tokens(data):
    lexer = Lexer(data)

    tokens = []
    while True:
        token = lexer.next()
        if token == "end":
            break
        tokens.append(token)

    return tokens


def part_a(tokens):
    product = 0
    for i, token in enumerate(tokens):
        if (token == "mul" and tokens[i+1] == '('
                and isinstance(tokens[i+2], int)
                and tokens[i+3] == ','
                and isinstance(tokens[i+4], int)
                and tokens[i+5] == ')'):
            product += (tokens[i+2] * tokens[i+4])

    return product


def part_b(tokens):
    product = 0
    allow = True

    for i, token in enumerate(tokens):
        if token == "do":
            allow = True
        elif token == "dont":
            allow = False
        elif (token == "mul" and tokens[i+1] == '('
                and isinstance(tokens[i+2], int)
                and tokens[i+3] == ','
                and isinstance(tokens[i+4], int)
                and tokens[i+5] == ')'):
            if allow:
                product += (tokens[i+2] * tokens[i+4])

    return product


def main():
    tokens = get_tokens(get_data(day=3, year=2024))
    answer1 = part_a(tokens)
    print(f"The product is: {answer1}")
    answer2 = part_b(tokens)
    print(f"The restricted product is: {answer2}")


if __name__ == "__main__":
    main()

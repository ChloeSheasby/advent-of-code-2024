from aocd import get_data


class RuleList(list):
    def __init__(self, iterable, rules):
        super().__init__(iterable)
        self.rules = rules

    def sort(self):
        for i in range(len(self)):
            done = True

            for j in range(len(self) - i - 1):
                if [self[j + 1], self[j]] in self.rules:
                    self[j], self[j + 1] = self[j + 1], self[j]
                    done = False

            if done:
                break


def read_puzzle_input_to_rules_and_pages():
    data = get_data(day=5, year=2024)

    rules = []
    pages = []

    for line in data.split("\n"):
        if line == "":
            continue

        if "|" not in line:
            pages.append(line.split(","))
        else:
            rules.append(line.split("|"))

    return rules, pages


def part_a(rules, pages):
    running_total = 0

    for page in pages:
        for i, _ in enumerate(page):
            if i == len(page) - 1:
                running_total += int(page[len(page) // 2])
                break
            if [page[i], page[i + 1]] not in rules:
                break

    return running_total


def part_b(rules, pages):
    running_total = 0

    pages_to_fix = []

    for page in pages:
        for i in range(len(page) - 1):
            if [page[i], page[i + 1]] not in rules:
                pages_to_fix.append(RuleList(page, rules))
                break

    for page in pages_to_fix:
        page.sort()
        running_total += int(page[len(page) // 2])

    return running_total


def main():
    rules, pages = read_puzzle_input_to_rules_and_pages()
    answer1 = part_a(rules, pages)
    print(
        f"The middle page total of the correctly-ordered updates is: {answer1}"
    )
    answer2 = part_b(rules, pages)
    print(
        f"The middle page total of the correctly-ordered updates is: {answer2}"
    )


if __name__ == "__main__":
    main()

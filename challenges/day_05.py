from aocd import get_data


# binary search tree class
class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, rule):
        temp = rule.split("|")
        if data < self.data:
            if self.left is None:
                self.left = BST(temp[0])
            else:
                self.left.insert(rule)
        else:
            if self.right is None:
                self.right = BST(temp[1])
            else:
                self.right.insert(rule)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements


def read_puzzle_input_to_rules_and_pages():
    data = get_data(day=5, year=2024)

    rules = []
    pages = []

    for line in data.split("\n"):
        if line == "":
            continue

        # check if line has | in it
        if "|" not in line:
            pages.append(line.split(","))
        else:
            rules.append(line)

    return rules, pages


def put_rules_in_order(rules):
    ordered_rules = []

    for rule in rules:
        temp = rule.split("|")
        if temp[0] in ordered_rules:
            ordered_rules.insert(ordered_rules.index(temp[0]) + 1, temp[1])
        elif temp[1] in ordered_rules:
            ordered_rules.insert(ordered_rules.index(temp[1]), temp[0])
        else:
            rules.append(rule)

    return ordered_rules



    # rules.sort(key=lambda x: x.split("|")[1])

    # rule_counts = {}
    # for rule in rules:
    #     temp = rule.split("|")
    #     rule_number = temp[1]
    #     if rule_number in rule_counts:
    #         rule_counts[rule_number] += 1
    #     else:
    #         rule_counts[rule_number] = 1

    # rule_counts = dict(sorted(rule_counts.items(), key=lambda item: item[1]))

    # print(rule_counts)

    # rule_counts = {}
    # for rule in rules:
    #     temp = rule.split("|")
    #     rule_number = temp[0]
    #     if rule_number in rule_counts:
    #         rule_counts[rule_number] += 1
    #     else:
    #         rule_counts[rule_number] = 1

    # rule_counts = dict(sorted(rule_counts.items(), key=lambda item: item[1]))

    # print(rule_counts)

    # ordered_rules = list(rule_counts.keys())

    # #find what values from the first part of the rule are not in the second part
    # # add those to the beginning of the ordered_rules list
    # for rule in rules:
    #     temp = rule.split("|")
    #     if temp[0] not in ordered_rules:
    #         ordered_rules.insert(0, temp[0])

    # return ordered_rules


def part_a(rules, pages):
    ordered_rules = put_rules_in_order(rules)

    print(ordered_rules)

    running_total = 0

    for page in pages:
        # compare page to ordered_rules to check the order of the items in the page
        for i in range(len(page) - 1):
            if ordered_rules.index(page[i]) > ordered_rules.index(page[i + 1]):
                break
        else:
            # add the middle of the page to the total
            running_total += int(page[int(len(page) / 2)])

    return running_total


def main():
    rules, pages = read_puzzle_input_to_rules_and_pages()
    answer1 = part_a(rules, pages)
    print(f"The middle page total of the correctly-ordered updates is: {answer1}")


if __name__ == "__main__":
    main()

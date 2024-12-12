import pytest

from challenges.day_05 import part_a


class TestDay05():
    @pytest.fixture(autouse=True)
    def setUp(self) -> None:
        self.rules = [
            "47|53",
            "97|13",
            "97|61",
            "97|47",
            "75|29",
            "61|13",
            "75|53",
            "29|13",
            "97|29",
            "53|29",
            "61|53",
            "97|53",
            "61|29",
            "47|13",
            "75|47",
            "97|75",
            "47|61",
            "75|61",
            "47|29",
            "75|13",
            "53|13"
        ]
        self.pages = [
            ["75", "47", "61", "53", "29"],
            ["97", "61", "53", "29", "13"],
            ["75", "29", "13"],
            ["75", "97", "47", "61", "53"],
            ["61", "13", "29"],     
            ["97", "13", "75", "29", "47"]
        ]

    # def test_given_small_input_when_part_a_correct_answer_given(
    #         self):
    #     expected = 143

    #     result = part_a(self.rules, self.pages)

    #     assert expected == result

    # def test_given_large_input_when_part_a_correct_answer_given(
    #         self):
    #     expected = 2397

    #     array = read_puzzle_input_to_nested_array()

    #     result = part_a(array)

    #     assert expected == result

    # def test_given_small_input_when_part_b_correct_answer_given(
    #         self):
    #     expected = 9

    #     result = part_b(self.array)

    #     assert expected == result

    # def test_given_large_input_when_part_b_correct_answer_given(
    #         self):
    #     expected = 1824

    #     array = read_puzzle_input_to_nested_array()

    #     result = part_b(array)

    #     assert expected == result

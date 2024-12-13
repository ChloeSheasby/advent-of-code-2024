import pytest

from challenges.day_05 import (part_a, part_b,
                               read_puzzle_input_to_rules_and_pages)


class TestDay05():
    @pytest.fixture(autouse=True)
    def setUp(self) -> None:
        self.rules = [
            ["47", "53"],
            ["97", "13"],
            ["97", "61"],
            ["97", "47"],
            ["75", "29"],
            ["61", "13"],
            ["75", "53"],
            ["29", "13"],
            ["97", "29"],
            ["53", "29"],
            ["61", "53"],
            ["97", "53"],
            ["61", "29"],
            ["47", "13"],
            ["75", "47"],
            ["97", "75"],
            ["47", "61"],
            ["75", "61"],
            ["47", "29"],
            ["75", "13"],
            ["53", "13"]
        ]
        self.pages = [
            ["75", "47", "61", "53", "29"],
            ["97", "61", "53", "29", "13"],
            ["75", "29", "13"],
            ["75", "97", "47", "61", "53"],
            ["61", "13", "29"],
            ["97", "13", "75", "29", "47"]
        ]

    def test_given_small_input_when_part_a_correct_answer_given(
            self):
        expected = 143

        result = part_a(self.rules, self.pages)

        assert expected == result

    def test_given_large_input_when_part_a_correct_answer_given(
            self):
        expected = 5639

        rules, pages = read_puzzle_input_to_rules_and_pages()

        result = part_a(rules, pages)

        assert expected == result

    def test_given_small_input_when_part_b_correct_answer_given(
            self):
        expected = 123

        result = part_b(self.rules, self.pages)

        assert expected == result

    def test_given_large_input_when_part_b_correct_answer_given(
            self):
        expected = 5273

        rules, pages = read_puzzle_input_to_rules_and_pages()

        result = part_b(rules, pages)

        assert expected == result

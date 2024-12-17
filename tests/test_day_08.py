import pytest

from challenges.day_08 import part_a, part_b, read_puzzle_input_to_map


class TestDay08():
    @pytest.fixture(autouse=True)
    def setUp(self) -> None:
        self.map = [
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "0", ".", ".", "."],
            [".", ".", ".", ".", ".", "0", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "0", ".", ".", ".", "."],
            [".", ".", ".", ".", "0", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "A", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "A", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "A", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
        ]

        self.map2 = [
            ["T", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "T", ".", ".", ".", ".", ".", "."],
            [".", "T", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
        ]

    def test_given_small_input_when_part_a_correct_answer_given(
            self):
        expected = 14

        result = part_a(self.map)

        assert expected == result

    def test_given_large_input_when_part_a_correct_answer_given(
            self):
        expected = 254

        map = read_puzzle_input_to_map()

        result = part_a(map)

        assert expected == result

    def test_given_small_input_when_part_b_correct_answer_given(
            self):
        expected = 34

        result = part_b(self.map)

        assert expected == result

    def test_given_second_small_input_when_part_b_correct_answer_given(
            self):
        expected = 9

        result = part_b(self.map2)

        assert expected == result

    def test_given_large_input_when_part_b_correct_answer_given(
            self):
        expected = 951

        map = read_puzzle_input_to_map()

        result = part_b(map)

        assert expected == result

import pytest

from challenges.day_04 import part_a, part_b, read_puzzle_input_to_nested_array


class TestDay04():
    @pytest.fixture(autouse=True)
    def setUp(self) -> None:
        self.array = [
            ['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'],
            ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A'],
            ['A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M'],
            ['M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X'],
            ['X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M'],
            ['X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A'],
            ['S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S'],
            ['S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A'],
            ['M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M'],
            ['M', 'X', 'M', 'X', 'A', 'X', 'M', 'A', 'S', 'X']
        ]

    def test_given_small_input_when_part_a_correct_answer_given(
            self):
        expected = 18

        result = part_a(self.array)

        assert expected == result

    def test_given_large_input_when_part_a_correct_answer_given(
            self):
        expected = 2397

        array = read_puzzle_input_to_nested_array()

        result = part_a(array)

        assert expected == result

    def test_given_small_input_when_part_b_correct_answer_given(
            self):
        expected = 9

        result = part_b(self.array)

        assert expected == result

    def test_given_large_input_when_part_b_correct_answer_given(
            self):
        expected = 1824

        array = read_puzzle_input_to_nested_array()

        result = part_b(array)

        assert expected == result

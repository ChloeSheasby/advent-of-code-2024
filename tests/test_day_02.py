import pytest

from day_02 import part_a, part_b, read_puzzle_input_to_nested_array


class TestDayOne():
    @pytest.fixture(autouse=True)
    def setUp(self) -> None:
        self.array = [
            [7, 6, 4, 2, 1],
            [1, 2, 7, 8, 9],
            [9, 7, 6, 2, 1],
            [1, 3, 2, 4, 5],
            [8, 6, 4, 4, 1],
            [1, 3, 6, 7, 9]
        ]

    def test_given_small_input_when_part_a_correct_answer_given(
            self):
        expected = 2

        result = part_a(self.array)

        assert expected == result

    def test_given_large_input_when_part_a_correct_answer_given(
            self):
        array = read_puzzle_input_to_nested_array()
        expected = 257

        result = part_a(array)

        assert expected == result

    def test_given_small_input_when_part_b_correct_answer_given(self):
        expected = 4

        result = part_b(self.array)

        assert expected == result

    def test_given_large_input_when_part_b_correct_answer_given(self):
        array = read_puzzle_input_to_nested_array()
        expected = 328

        result = part_b(array)

        assert expected == result

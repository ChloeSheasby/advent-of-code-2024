import pytest

from day_two.day_two import (calculate_possible_safety, calculate_safety,
                             read_puzzle_input_to_nested_array)


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

    def test_given_small_input_when_calculate_safety_correct_answer_given(
            self):
        expected = 2

        result = calculate_safety(self.array)

        assert expected == result

    def test_given_large_input_when_calculate_safety_correct_answer_given(
            self):
        array = read_puzzle_input_to_nested_array()
        expected = 257

        result = calculate_safety(array)

        assert expected == result

    def test_given_small_input_when_calculate_possible_safety_correct_answer_given(
            self):
        expected = 4

        result = calculate_possible_safety(self.array)

        assert expected == result

    def test_given_large_input_when_calculate_possible_safety_correct_answer_given(
            self):
        array = read_puzzle_input_to_nested_array()
        expected = 328

        result = calculate_possible_safety(array)

        assert expected == result

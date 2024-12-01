import pytest

from day_one.day_one import (calculate_distance, calculate_similarity,
                             read_puzzle_input_to_arrays)


class TestDayOne():
    @pytest.fixture(autouse=True)
    def setUp(self) -> None:
        self.array1 = [3, 4, 2, 1, 3, 3]
        self.array2 = [4, 3, 5, 3, 9, 3]

    def test_given_small_input_when_calculate_distance_correct_answer_given(
            self):
        expected = 11

        result = calculate_distance(self.array1, self.array2)

        assert expected == result

    def test_given_large_input_when_calculate_distance_correct_answer_given(
            self):
        array1, array2 = read_puzzle_input_to_arrays()
        expected = 2756096

        result = calculate_distance(array1, array2)

        assert expected == result

    def test_given_small_input_when_calculate_similarity_correct_answer_given(
            self):
        expected = 31

        result = calculate_similarity(self.array1, self.array2)

        assert expected == result

    def test_given_large_input_when_calculate_similarity_correct_answer_given(
            self):
        array1, array2 = read_puzzle_input_to_arrays()
        expected = 23117829

        result = calculate_similarity(array1, array2)

        assert expected == result

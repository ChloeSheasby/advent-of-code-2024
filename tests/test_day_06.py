import pytest

from challenges.day_06 import part_a, part_b, read_puzzle_input_to_nested_array


class TestDay06():
    @pytest.fixture(autouse=True)
    def setUp(self) -> None:
        self.map = [
            [".", ".", ".", ".", "#", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "#", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "#", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "#", ".", ".", "^", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "#", "."],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "#", ".", ".", "."]
        ]

    def test_given_small_input_when_part_a_correct_answer_given(
            self):
        expected = 41

        result = part_a(self.map)

        assert expected == result

    def test_given_large_input_when_part_a_correct_answer_given(
            self):
        expected = 5131

        map = read_puzzle_input_to_nested_array()

        result = part_a(map)

        assert expected == result

    def test_given_small_input_when_part_b_correct_answer_given(
            self):
        expected = 6

        result = part_b(self.map)

        assert expected == result

    # def test_given_large_input_when_part_b_correct_answer_given(
    #         self):
    #     expected = 1824

    #     array = read_puzzle_input_to_nested_array()

    #     result = part_b(array)

    #     assert expected == result

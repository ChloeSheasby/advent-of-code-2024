import pytest

from challenges.day_10 import part_a, read_puzzle_input_to_map


class TestDay10():
    @pytest.fixture(autouse=True)
    def setUp(self) -> None:
        self.test_1 = [
            ["0", "1", "2", "3"],
            ["1", "2", "3", "4"],
            ["8", "7", "6", "5"],
            ["9", "8", "7", "6"]
        ]

        self.test_2 = [
            [".", ".", ".", "0", ".", ".", "."],
            [".", ".", ".", "1", ".", ".", "."],
            [".", ".", ".", "2", ".", ".", "."],
            ["6", "5", "4", "3", "4", "5", "6"],
            ["7", ".", ".", ".", ".", ".", "7"],
            ["8", ".", ".", ".", ".", ".", "8"],
            ["9", ".", ".", ".", ".", ".", "9"]
        ]

        self.test_3 = [
            [".", ".", "9", "0", ".", ".", "9"],
            [".", ".", ".", "1", ".", "9", "8"],
            [".", ".", ".", "2", ".", ".", "7"],
            ["6", "5", "4", "3", "4", "5", "6"],
            ["7", "6", "5", ".", "9", "8", "7"],
            ["8", "7", "6", ".", ".", ".", "."],
            ["9", "8", "7", ".", ".", ".", "."]
        ]

        self.test_4 = [
            ["1", "0", ".", ".", "9", ".", "."],
            ["2", ".", ".", ".", "8", ".", "."],
            ["3", ".", ".", ".", "7", ".", "."],
            ["4", "5", "6", "7", "6", "5", "4"],
            [".", ".", ".", "8", ".", ".", "3"],
            [".", ".", ".", "9", ".", ".", "2"],
            [".", ".", ".", ".", ".", "0", "1"]
        ]

        self.test_5 = [
            ["8", "9", "0", "1", "0", "1", "2", "3"],
            ["7", "8", "1", "2", "1", "8", "7", "4"],
            ["8", "7", "4", "3", "0", "9", "6", "5"],
            ["9", "6", "5", "4", "9", "8", "7", "4"],
            ["4", "5", "6", "7", "8", "9", "0", "3"],
            ["3", "2", "0", "1", "9", "0", "1", "2"],
            ["0", "1", "3", "2", "9", "8", "0", "1"],
            ["1", "0", "4", "5", "6", "7", "3", "2"]
        ]

    def test_given_small_input_1_when_part_a_correct_answer_given(
            self):
        expected = 1

        result = part_a(self.test_1)

        assert expected == result

    def test_given_small_input_2_when_part_a_correct_answer_given(
            self):
        expected = 2

        result = part_a(self.test_2)

        assert expected == result

    def test_given_small_input_3_when_part_a_correct_answer_given(
            self):
        expected = 4

        result = part_a(self.test_3)

        assert expected == result

    def test_given_small_input_4_when_part_a_correct_answer_given(
            self):
        expected = 3

        result = part_a(self.test_4)

        assert expected == result

    def test_given_small_input_5_when_part_a_correct_answer_given(
            self):
        expected = 36

        result = part_a(self.test_5)

        assert expected == result

    def test_given_large_input_when_part_a_correct_answer_given(
            self):
        expected = 816

        topo_map = read_puzzle_input_to_map()

        result = part_a(topo_map)

        assert expected == result

    # def test_given_small_input_when_part_b_correct_answer_given(
    #         self):
    #     expected = 2858

    #     result = part_b(self.files, self.space)

    #     assert expected == result

    # def test_given_second_small_input_when_part_b_correct_answer_given(
    #         self):
    #     expected = 6448168620520

    #     files, space = read_puzzle_input_to_dict()

    #     result = part_b(files, space)

    #     assert expected == result

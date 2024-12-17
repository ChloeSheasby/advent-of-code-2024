import pytest

from challenges.day_09 import part_a, part_b, read_puzzle_input_to_dict


class TestDay09():
    @pytest.fixture(autouse=True)
    def setUp(self) -> None:
        self.files = [2, 3, 1, 3, 2, 4, 4, 3, 4, 2]
        self.space = [3, 3, 3, 1, 1, 1, 1, 1, 0]

    def test_given_small_input_when_part_a_correct_answer_given(
            self):
        expected = 1928

        result = part_a(self.files, self.space)

        assert expected == result

    def test_given_large_input_when_part_a_correct_answer_given(
            self):
        expected = 6421128769094

        files, space = read_puzzle_input_to_dict()

        result = part_a(files, space)

        assert expected == result

    def test_given_small_input_when_part_b_correct_answer_given(
            self):
        expected = 2858

        result = part_b(self.files, self.space)

        assert expected == result

    def test_given_second_small_input_when_part_b_correct_answer_given(
            self):
        expected = 6448168620520

        files, space = read_puzzle_input_to_dict()

        result = part_b(files, space)

        assert expected == result

import pytest
from aocd import get_data

from challenges.day_07 import part_a, part_b


class TestDay07():
    @pytest.fixture(autouse=True)
    def setUp(self) -> None:
        self.data = """190: 10 19
            3267: 81 40 27
            83: 17 5
            156: 15 6
            7290: 6 8 6 15
            161011: 16 10 13
            192: 17 8 14
            21037: 9 7 18 13
            292: 11 6 16 20 15"""

    # test cases don't work but normal cases do?
    def test_given_small_input_when_part_a_correct_answer_given(
            self):
        expected = 3749

        result = part_a(self.data)

        assert expected == result

    def test_given_large_input_when_part_a_correct_answer_given(
            self):
        expected = 303766880536

        data = get_data(day=7, year=2024)

        result = part_a(data)

        assert expected == result

    def test_given_small_input_when_part_b_correct_answer_given(
            self):
        expected = 11387

        result = part_b(self.data)

        assert expected == result

    def test_given_large_input_when_part_b_correct_answer_given(
            self):
        expected = 337041851384440

        data = get_data(day=7, year=2024)

        result = part_b(data)

        assert expected == result

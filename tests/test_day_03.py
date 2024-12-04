import pytest
from aocd import get_data

from challenges.day_03 import get_tokens, part_a, part_b


class TestDay03():
    @pytest.fixture(autouse=True)
    def setUp(self) -> None:
        self.data_a = (
            "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]"
            "then(mul(11,8)mul(8,5))"
        )
        self.tokens_a = get_tokens(self.data_a)
        self.data_b = (
            "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64]"
            "(mul(11,8)undo()?mul(8,5))"
        )
        self.tokens_b = get_tokens(self.data_b)

    def test_given_small_input_when_part_a_correct_answer_given(
            self):
        expected = 161

        result = part_a(self.tokens_a)

        assert expected == result

    def test_given_large_input_when_part_a_correct_answer_given(
            self):
        tokens = get_tokens(get_data(day=3, year=2024))

        expected = 188192787

        result = part_a(tokens)

        assert expected == result

    def test_given_small_input_when_part_b_correct_answer_given(
            self):
        expected = 48

        result = part_b(self.tokens_b)

        assert expected == result

    def test_given_large_input_when_part_b_correct_answer_given(
            self):
        tokens = get_tokens(get_data(day=3, year=2024))

        expected = 113965544

        result = part_b(tokens)

        assert expected == result

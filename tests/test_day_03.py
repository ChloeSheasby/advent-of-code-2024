import pytest

from challenges.day_03 import part_a


class TestDay03():
    @pytest.fixture(autouse=True)
    def setUp(self) -> None:
        self.data = (
            "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]"
            "then(mul(11,8)mul(8,5))"
        )

    def test_given_small_input_when_part_a_correct_answer_given(
            self):
        expected = 161

        result = part_a(self.data)

        assert expected == result

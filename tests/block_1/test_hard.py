import pytest
from block_1.hard import sum_args_with_required_args


@pytest.mark.parametrize("num_1, num_2, num_3, num_4, args, kwargs, expected_value",
                         [(1, 2, 3, 4, (5, 6, 7), {}, 28),
                          (1, 1, 1, 1, (1, 1, 1), {'num_8': 1}, 7)])
def test_sum_args_with_required_args(num_1, num_2, num_3, num_4, args, kwargs, expected_value):
    assert sum_args_with_required_args(num_1, num_2, num_3, num_4, *args, **kwargs) == expected_value

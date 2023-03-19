import pytest
from block_1.medium import sum_args, sum_args_with_required_args


@pytest.mark.parametrize("args, expected_result", [([1, 2, 3, 4, 5], 15),
                                                   ([1, 1, 1], 3)])
def test_sum_args(args: list, expected_result: int):
    assert sum_args(*args) == expected_result


def test_sum_args_with_required_args_exception():
    with pytest.raises(TypeError):
        sum_args_with_required_args(1)

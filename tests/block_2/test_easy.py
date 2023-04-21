import pytest

from block_2.easy import sum_args, get_calls_cnt, refresh_calls_cnt


@pytest.fixture(autouse=True)
def clean_counter():
    """Очищает счетчик"""
    refresh_calls_cnt()


@pytest.mark.parametrize('launch_numbers, expected',
                         [(6, 6),
                          (15, 15)])
def test_sum_args(launch_numbers: int, expected: int):
    for _ in range(launch_numbers):
        sum_args(1, 2)
    assert expected == get_calls_cnt()


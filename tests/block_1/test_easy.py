import pytest
from block_1.easy import string_multiplier

@pytest.mark.parametrize("string, multiplier, expected_result",
                         [('test', 3, 'testTESTtest')])
def test_string_multiplier(string: str, multiplier: int, expected_result: str):
    assert string_multiplier(string=string, multiplier=multiplier) == expected_result
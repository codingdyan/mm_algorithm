import pytest
from majority_element import find_majority_element

# Positive test cases
@pytest.mark.parametrize("test_input,expected", [
    ([3, 3, 4, 2, 4, 4, 2, 4, 4], 4),
    ([1, 1, 1, 1], 1),
    ([2, 2, 2, 1, 1], 2),
    ([1, 1, 2, 2, 2], 2),
    ([5], 5),
])
def test_find_majority_element_positive(test_input, expected):
    assert find_majority_element(test_input) == expected

# Negative test cases
@pytest.mark.parametrize("test_input,expected", [
    ([3, 1, 2, 4], None),
    ([1, 2], None),
    ([4, 4, 2, 2], None),
    ([], None),
    ([1, 2, 3, 1], None),
])
def test_find_majority_element_negative(test_input, expected):
    assert find_majority_element(test_input) == expected

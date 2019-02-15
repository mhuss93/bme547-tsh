import pytest


@pytest.mark.parametrize("input, expected", [
    ([1.0, 1.3, 1.7, 2.9, 3.3, 3.8, 4.0], "normal thyroid function"),
    ([0.7, 0.8, 1.2, 1.8, 2.9, 3.3, 3.5], "hyperthyroidism"),
    ([2.3, 2.5, 3.5, 3.6, 3.6, 4.3, 4.4], "hypothyroidism"),
])
def test_get_diagnosis(input, expected):
    from tsh import get_diagnosis

    answer = get_diagnosis(input)

    assert answer == expected

import pytest
from example import compute_fibonacci


@pytest.mark.parametrize("value, exptected_output", [(0,0),(1,1),(2,1),(3,2), (5,5),(10,55)])
def test_compute_fibonacci_with_expected_inputs(value, exptected_output):
    assert compute_fibonacci(value) == exptected_output

@pytest.mark.parametrize("value", [-1, 2.5, "3"])
def test_compute_fibonacci_with_wrong_inputs(value):
    with pytest.raises(ValueError):
        compute_fibonacci(value)

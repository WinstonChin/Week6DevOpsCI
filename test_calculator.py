import pytest
from calculator import add, subtract, multiply, divide

@pytest.mark.basic
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

@pytest.mark.basic
def test_subtract():
    assert subtract(5, 3) == 2

@pytest.mark.edge
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

@pytest.mark.slow
def test_performance_multiply():
    # example "slow" test (you can simulate a longer run with a loop)
    for _ in range(100000):
        multiply(3, 4)
    assert multiply(3, 4) == 12

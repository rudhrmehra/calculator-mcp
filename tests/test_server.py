import pytest

from server import (
    add,
    subtract,
    multiply,
    divide,
    power,
    square_root,
    factorial,
    is_prime,
    find_gcd,
    find_lcm,
    modulus,
)

# --- Basic Arithmetic Tests ---

def test_add():
    assert add(5, 8) == 13
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3, 7) == 21

def test_divide():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    # Test that division by zero raises a ValueError
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

# --- Advanced Math Operations Tests ---

def test_power():
    assert power(2, 3) == 8

def test_square_root():
    assert square_root(16) == 4.0

def test_square_root_negative():
    with pytest.raises(ValueError):
        square_root(-4)

def test_factorial():
    assert factorial(5) == 120

def test_is_prime():
    assert is_prime(7) is True
    assert is_prime(4) is False
    assert is_prime(1) is False

def test_find_gcd():
    assert find_gcd(123456, 789012) == 12

def test_find_lcm():
    assert find_lcm(4, 6) == 12

def test_modulus():
    assert modulus(10, 3) == 1
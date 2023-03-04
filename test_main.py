import pytest

from main import mul


def test_mul():
    assert mul(2, 3) == 6


def test_mul_zero():
    assert mul(1, 0) == 0


def test_mul_error():
    with pytest.raises(TypeError):
        mul("a", "b")
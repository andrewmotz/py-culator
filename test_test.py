import pytest

from run import subtraction

def test_subtraction_pos():
    assert subtraction(5, 2) == 3

def test_subtraction_nrg():
    assert subtraction(3, 5) == 2

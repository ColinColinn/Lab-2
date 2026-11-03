import pytest
import exercise6 as Lab2


# ---------- find_min_max() ----------
def test_find_min_max_positive():
    result = Lab2.find_min_max([5, 67, 32])
    assert result == [5, 67]

def test_find_min_max_negative():
    result = Lab2.find_min_max([-3, 10, -15, 0])
    assert result == [-15, 10]

def test_find_min_max_single_value():
    result = Lab2.find_min_max([25])
    assert result == [25, 25]


# ---------- calc_average() ----------
def test_calc_average_whole_number():
    result = Lab2.calc_average([10, 20, 30])
    assert result == 20

def test_calc_average_decimal():
    result = Lab2.calc_average([1, 2, 2])
    assert result == pytest.approx(1.6667, abs=0.001)


# ---------- calc_median_temperature() ----------
def test_calc_median_odd_count():
    result = Lab2.calc_median_temperature([5, 1, 3])
    assert result == 3

def test_calc_median_even_count():
    result = Lab2.calc_median_temperature([4, 1, 3, 2])
    assert result == 2.5
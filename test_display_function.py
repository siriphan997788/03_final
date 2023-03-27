from function import display_rang
import pytest

@pytest.mark.parametrize('input_number,expected_result', [(0,"Out of bounds, enter an integer value."),(-1,"Out of bounds, enter an integer value."),
(-0.1,"Out of bounds, enter an integer value."),(1.1,"Out of bounds, enter an integer value."),("a","Out of bounds, enter an integer value."),
("#","Out of bounds, enter an integer value."),(0.5,"Out of bounds, enter an integer value."),(-1.5,"Out of bounds, enter an integer value."),
(1.5,"Out of bounds, enter an integer value.")])


@pytest.mark.display #pytest -m display
def test_display(input_number,expected_result):
    actual_result = display_rang(input_number)
    assert expected_result == actual_result
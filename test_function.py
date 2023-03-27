from function import validate_number
import pytest


@pytest.mark.validate 
def test_out_of_range_input_0():
    input = 0
    expected_result = "Out of bounds, enter an integer value."
    actual_result = validate_number(input)
    assert expected_result == actual_result


@pytest.mark.validate
def test_out_of_range_input_0():
    input = -1
    expected_result = "Out of bounds, enter an integer value."
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate
def test_out_of_range_input_0():
    input = -0.1
    expected_result = "Out of bounds, enter an integer value."
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate 
def test_input_integer_input_1_1():
    input = 1.1
    expected_result = "Out of bounds, enter an integer value."
    actual_result = validate_number(input)
    assert expected_result == actual_result


@pytest.mark.validate 
def test_input_integer_input_a():
    input = "a"
    expected_result = "input integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate
def test_input_integer_input_sharp():
    input = "#"
    expected_result = "input integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result


    
@pytest.mark.validate
def test_out_of_range_input_0_5():
    input = 0.5
    expected_result = "Out of bounds, enter an integer value."
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate
def test_out_of_range_input_1_5():
    input = -1.5
    expected_result = "Out of bounds, enter an integer value."
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate
def test_input_integer_input_1_5():
    input = 1.5
    expected_result = "Out of bounds, enter an integer value."
    actual_result = validate_number(input)
    assert expected_result == actual_result


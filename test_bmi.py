import pytest
import bmi

# Boundary for Underweight
@pytest.mark.parametrize("input,expected", [(0.00, "0.00; Underweight."), (18.49, "18.49; Underweight."), (18.50, "18.50; Normal weight.")])
def test_output_underweight(input, expected):
    assert bmi.output(input) == expected

# Boundary for Normal weight
@pytest.mark.parametrize("input,expected", [(18.49, "18.49; Underweight."), (18.50, "18.50; Normal weight."), (24.90, "24.90; Normal weight."), (25.00, "25.00; Overweight.")])
def test_output_normal(input, expected):
    assert bmi.output(input) == expected

# Boundary for Overweight
@pytest.mark.parametrize("input,expected", [(24.99, "24.99; Normal weight."), (25.00, "25.00; Overweight."), (29.99, "29.99; Overweight."), (30.00, "30.00; Obese.")])
def test_output_over(input, expected):
    assert bmi.output(input) == expected

# Boundary for Obese
@pytest.mark.parametrize("input,expected", [(29.99, "29.99; Overweight."), (30.00, "30.00; Obese.")])
def test_output_obese(input, expected):
    assert bmi.output(input) == expected
import pytest
from .functions import bmicalculations

def geninputs():
    inputs = ["0.01", "0.01", "1.00", "1.00", "1.00", "0.00", "1.00", "1.00", "1.00", "1.00", "1.00", "-0.01", "0.00", "0.00", "1.00"]
    for item in inputs:
        yield item

#GEN = geninputs()
#@pytest.mark.parametrize("expected", [([0.01, 0.01, 1.00]), ([1.00, 1.00, 0.00]), ([1.0, 1.0, 1.0])])
#def test_user_input(expected, monkeypatch):
#    monkeypatch.setattr('builtins.input', lambda _: next(GEN))
#    assert user_input() == expected
#
#def test_user_input_error(monkeypatch):
#    monkeypatch.setattr('builtins.input', lambda _: next(GEN))
#    with pytest.raises(ValueError):
#        user_input()

# Boundary for Underweight
@pytest.mark.parametrize("input,expected", [(15.00, "15.00; Underweight."), (18.49, "18.49; Underweight."), (18.50, "18.50; Normal weight."), (20.10, "20.10; Normal weight."), (24.99, "24.99; Normal weight."), (25.00, "25.00; Overweight."), (27.50, "27.50; Overweight."), (29.99, "29.99; Overweight."), (30.00, "30.00; Obese."), (35.00, "35.00; Obese.")])
def test_output(input, expected):
    assert bmicalculations.output(input) == expected

@pytest.mark.parametrize("feet, inches, pounds, expected", [(0.01, 0.01, 0.01, 426.04), (1.00, 1.00, 0.00, 0.00), (1.0, 1.0, 1.0, 4.26)])
def test_calculate_bmi(feet, inches, pounds, expected):
    assert bmicalculations.calculate_bmi(feet, inches, pounds) == expected 

@pytest.mark.parametrize("feet, inches, pounds", [(0.00, 0.00, 1.00), (1.00, 1.00, -0.01)])
def test_calculate_bmi_error(feet, inches, pounds):
    with pytest.raises(ValueError):
        bmicalculations.calculate_bmi(feet, inches, pounds)
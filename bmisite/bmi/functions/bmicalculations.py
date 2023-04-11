def calculate_bmi(feet, inches, pounds):
    weight = pounds * 0.45
    height = ((feet * 12.0) + inches) * 0.025
    if (weight < 0.00) or (height <= 0.00):
        raise ValueError("User inputs must be positive values.")
    bmi = weight / (height ** 2.0) 
    return round(bmi, 2)

def output(user_bmi):
    output = "{:.2f}".format(user_bmi) + "; "
    if user_bmi < 18.5:
        output += "Underweight."
    elif user_bmi < 25.0:
        output += "Normal weight."
    elif user_bmi < 30.0:
        output += "Overweight."
    else:
        output += "Obese."

    return output
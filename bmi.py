def main():
    uservalues = user_input()
    feet, inches, pounds = uservalues[0], uservalues[1], uservalues[2]
    user_bmi = calculate_bmi(feet, inches, pounds)
    print(output(user_bmi))

def user_input():
    feet = float(input("Enter your height in feet: "))
    inches = float(input("Enter your remaining height in inches: "))
    pounds = float(input("Enter your weight in pounds: "))

    if ((feet + inches) <= 0.00) or (pounds < 0.00):
        raise ValueError("User input must be positive values.")

    res = [feet, inches, pounds]
    return res

def calculate_bmi(feet, inches, pounds):
    weight = pounds * 0.45
    height = ((feet * 12.0) + inches) * 0.025
    if (weight < 0.00) or (height <= 0.00):
        raise ValueError("User inputs must be positive values.")
    bmi = weight / (height ** 2.0) 
    return round(bmi, 2)

def output(user_bmi):
    output = "{:.2f}".format(user_bmi) + "; "
    if user_bmi < 18.6:
        output += "Underweight."
    elif user_bmi < 25.0:
        output += "Normal weight."
    elif user_bmi < 30.0:
        output += "Overweight."
    else:
        output += "Obese."

    return output

if __name__=="__main__":
    main()

def calculate_bmi(feet, inches, pounds):
    kilos = conv_lbs_kilos(pounds)
    inches += conv_ft_in(feet)
    meters = conv_in_m(inches)
    bmi = kilos / (meters ** 2.0) 
    return bmi

def conv_lbs_kilos(lbs):
    return lbs * 0.45
def conv_ft_in(ft):
    return feet * 12.0
def conv_in_m(inches):
    return inches* 0.025


def generate_output(bmi):
    output = str(bmi) + "; "
    if user_bmi < 18.5:
        output += "Underweight."
    elif user_bmi < 24.9:
        output += "Normal weight."
    elif user_bmi < 29.9:
        output += "Overweight."
    else:
        output += "Obese."

    return output

feet = float(input("Enter your height in feet: "))
inches = float(input("Enter your remaining height in inches: "))
pounds = float(input("Enter your weight in pounds: "))

user_bmi = calculate_bmi(feet, inches, pounds)
print(generate_output(user_bmi))
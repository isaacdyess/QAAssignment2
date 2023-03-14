def main():
    feet, inches, pounds = user_input()
    user_bmi = calculate_bmi(feet, inches, pounds)
    print(output(user_bmi))

def user_input():
    feet = float(input("Enter your height in feet: "))
    inches = float(input("Enter your remaining height in inches: "))
    pounds = float(input("Enter your weight in pounds: "))

    return feet, inches, pounds

def calculate_bmi(feet, inches, pounds):
    kilos = conv_lbs_kilos(pounds)
    inches += conv_ft_in(feet)
    meters = conv_in_m(inches)
    bmi = kilos / (meters ** 2.0) 
    return round(bmi, 2)

def conv_lbs_kilos(lbs):
    return round(lbs * 0.45, 2)
def conv_ft_in(ft):
    return round(ft * 12.0, 2)
def conv_in_m(inches):
    return round(inches * 0.025, 2)


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

if __name__=="__main__":
    main()

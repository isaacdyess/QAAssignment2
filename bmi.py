def calculate_bmi(feet, inches, pounds):
    kilos = pounds * 0.45
    inches += (feet * 12.0)
    meters = inches * 0.025
    bmi = kilos / (meters ** 2.0) 
    return bmi

feet = float(input("Enter your height in feet: "))
inches = float(input("Enter your remaining height in inches: "))
pounds = float(input("Enter your weight in pounds: "))

user_bmi = calculate_bmi(feet, inches, pounds)
if user_bmi < 18.5:
    print(str(user_bmi) + "; Underweight.")
elif user_bmi < 24.9:
    print(str(user_bmi) + "; Normal weight.")
elif user_bmi < 29.9:
    print(str(user_bmi) + "; Overweight.")
else:
    print(str(user_bmi) + "; Obese.")
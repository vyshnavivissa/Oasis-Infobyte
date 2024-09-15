def bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    if bmi < 16:
        return "SEVERE THINNESS"
    elif bmi < 17:
        return "MODERATE THINNESS"
    elif bmi < 18.5:
        return "MILD THINNESS"
    elif bmi < 25:
        return "NORMAL"
    elif bmi < 30:
        return "OVERWEIGHT"
    elif bmi < 35:
        return "OBESE CLASS 1"
    elif bmi < 40:
        return "OBESE CLASS 2"
    else:
        return "OBESE CLASS 3"

weight_kg = float(input("Enter your weight (kg): "))
height_m = float(input("Enter your height (m): "))
print(bmi(weight_kg, height_m))

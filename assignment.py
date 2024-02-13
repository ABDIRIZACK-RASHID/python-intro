weight = float(input("Enter your weight in kilograms"))
hight = float(input("Enter your hight in meters"))
bmi = weight / (hight ** 2)
print(f"{bmi}")
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi <= 25:
    category = "normal"

elif 25 <= bmi < 29.9:
    category = "overwight"

else:
    category = "obese"
print(f"{category}")

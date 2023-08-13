print(" *** BMI ***")
w,h = input("Enter your weight(kg) and height(m) : ").split()
w = float(w)
h = float(h)

BMI = w / (h * h)

if BMI < 18.5:
    print("Your status is : Below normal weight.")
elif BMI >= 18.5 and BMI < 25:
    print("Your status is : Normal weight.")
elif BMI >= 25 and BMI < 30:
    print("Your status is : Overweight.")
elif BMI >= 30 and BMI < 35:
    print("Your status is : Case I Obesity.")
elif BMI >= 35 and BMI < 40:
    print("Your status is : Case II Obesity.")
elif BMI >= 40:
    print("Your status is : Case III Obesity.")
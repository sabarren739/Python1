# Python 1 Class
# Python Class 1 - Assignment 3 - Week 2 - CHALLENGE
# Scott Barren
#
# Challenge: Provide feedback to the user based on their BMI category
# (e.g., underweight, normal weight, overweight, obese).
#
# Input: Prompt the user to enter their weight in kilograms and height in meters.
# Processing: Calculate the BMI using the formula: BMI = Weight / (Height^2).
# Output: Display the calculated BMI.
#
# Input:
weight = float(input("Please enter your weight in kg: "))
height = float(input("Please enter your height in Meters: "))
#
# Processing:
BMI = weight / (height ** 2)
#
# Output
print("Your body mass index (BMI) is: " + str(BMI))
print("Your body mass index (BMI) should be between 18.5 and 24.9. ")
## print("Your body mass index (BMI) is: ", BMI)
#
if (BMI < 18.5):
    print("Gain some weight. Consult your Doctor")
elif (BMI > 24.9):
    print("Eat Healthier.  Get more Exercise.  Consult your Doctor")
else:
    print("Your BMI is good.  Always consult your Doctor")
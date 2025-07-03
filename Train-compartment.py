'''
Problem: Suggest which compartment to board based on passenger type.
- Age < 18: "General compartment or ask adult for help"
- Age 18-59 and gender is "female": "Ladies compartment available"
- Age 18-59 and gender is "male": "General compartment"
- Age >= 60: "Senior citizen compartment (if available) or general"
'''

age = int(input("Enter your age: "))
gender = input("Enter gender (male/female): ").lower()

if age < 18:
    print("General compartment or ask adult for help")
elif 18 <= age <= 59 and gender == "female":
    print("Ladies compartment available")
elif 18 <= age <= 59 and gender == "male":
    print("General compartment")
elif age >= 60:
    print("Senior citizen compartment (if available) or general")
else:           # you may skip this. However, I recommend providng an else block for better error handling.
    print("Please check your inputs")
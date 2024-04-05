def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI calculator!")
    weight = float(input("Please enter your weight in kilograms: "))
    height = float(input("Please enter your height in meters: "))

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print("Your BMI is: {:.2f}".format(bmi))
    print("You are classified as:", category)

if __name__ == "__main__":
    main()

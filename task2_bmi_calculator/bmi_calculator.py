"""
TASK 2 · BMI Calculator (Beginner Tier)
----------------------------------------
Command-line BMI calculator with input validation and category classification.

Checklist covered:
[x] Prompt user for weight (kg) and height (m) via command line
[x] Calculate BMI using the formula: BMI = weight / (height^2)
[x] Classify result into standard categories
[x] Display BMI rounded to 2 decimal places and the category
[x] Input validation: reject non-numeric input and negative values with a helpful error message
"""


def get_positive_float(prompt: str) -> float:
    """Keep asking until the user gives a valid positive number."""
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print(f"  ⚠  '{raw}' is not a valid number. Please enter a numeric value (e.g. 65.5).")
            continue

        if value <= 0:
            print(f"  ⚠  '{raw}' must be a positive number greater than 0. Try again.")
            continue

        return value


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    return weight_kg / (height_m ** 2)


def classify_bmi(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("=" * 45)
    print("        PYTHON BMI CALCULATOR")
    print("=" * 45)

    while True:
        weight = get_positive_float("Enter your weight in kg: ")
        height = get_positive_float("Enter your height in m (e.g. 1.75): ")

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        print("\n--- Result ---")
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category   : {category}")
        print("-" * 20)

        again = input("\nCalculate another BMI? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for using the BMI Calculator. Stay healthy!")
            break


if __name__ == "__main__":
    main()

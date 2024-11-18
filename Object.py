# main.py
"""
This module contains the main program for a BMI calculator.
"""

from bmi_calculator import BMICalculator

def get_user_input(unit_system: str) -> tuple:
    """Gets user input for weight and height based on the unit system.
    """
    if unit_system == "metric":
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in centimeters: "))
        return weight, height
    elif unit_system == "us":
        weight = float(input("Enter your weight in pounds: "))
        height_feet = int(input("Enter your height in feet: "))
        height_inches = int(input("Enter your height in inches: "))
        return weight, height_feet, height_inches
    else:
        raise ValueError("Invalid unit system.")

def display_bmi(bmi: float) -> None:
    """Displays the calculated BMI and its interpretation.
        bmi: The calculated BMI.
    """
    print(f"Your BMI is: {bmi:.1f}")
    print("BMI Legend:")
    print("Underweight: <18.5")
    print("Normal: 18.5 - 24.9")
    print("Overweight: 25 - 29.9")
    print("Obese: 30+")
    print("BMI Source: https://en.wikipedia.org/wiki/Body_mass_index")

def main():
    """Main function of the BMI calculator program."""
    while True:
        unit_system = input("Choose unit system (metric/us): ").lower()
        if unit_system not in ("metric", "us"):
            print("Invalid unit system. Please enter 'metric' or 'us'.")
            continue

        bmi_calculator = BMICalculator()

        if unit_system == "metric":
            weight, height = get_user_input(unit_system)
            bmi = bmi_calculator.calculate_bmi_metric(weight, height)
        elif unit_system == "us":
            weight, height_feet, height_inches = get_user_input(unit_system)
            bmi = bmi_calculator.calculate_bmi_us(weight, height_feet, height_inches)

        display_bmi(bmi)

        continue_calculation = input("Calculate BMI again? (yes/no): ").lower()
        if continue_calculation != "yes":
            break

if __name__ == "__main__":
    main()
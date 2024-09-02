POUNDS_TO_KG_CONVERSION_FACTOR = 0.453592
FEET_TO_CM_CONVERSION_FACTOR = 30.48
INCHES_TO_CM_CONVERSION_FACTOR = 2.54

# Here I use snake_case for variable names. I am also using docstrings to document each 
# function.
def get_user_weight():
  """Gets the user's weight in pounds."""
  return float(input("Enter your weight in pounds: "))


def get_user_height_feet():
  """Gets the user's height in feet."""
  return int(input("Enter your height in feet: "))


def get_user_height_inches():
  """Gets the user's height in inches."""
  return int(input("Enter your height in inches: "))


def convert_weight_to_kg(weight_pounds):
  """Converts weight from pounds to kilograms."""
  return weight_pounds * POUNDS_TO_KG_CONVERSION_FACTOR


def convert_height_to_cm(height_feet, height_inches):
  """Converts height from feet and inches to centimeters."""
  return (height_feet * FEET_TO_CM_CONVERSION_FACTOR) + (
      height_inches * INCHES_TO_CM_CONVERSION_FACTOR)


def calculate_bmi(weight_kg, height_cm):
  """Calculates the Body Mass Index (BMI)."""
  return weight_kg / ((height_cm / 100)**2)


def display_bmi(bmi):
  print(f"Your BMI is: {bmi:.1f}")
  print("BMI Legend:")
  print("Underweight: <18.5")
  print("Normal: 18.5 - 24.9")
  print("Overweight: 25 - 29.9")
  print("Obese: 30+")
  print("BMI Source: https://en.wikipedia.org/wiki/Body_mass_index")


def main():
  """Main function of the BMI calculator program."""
  weight_pounds = get_user_weight()
  height_feet = get_user_height_feet()
  height_inches = get_user_height_inches()

  weight_kg = convert_weight_to_kg(weight_pounds)
  height_cm = convert_height_to_cm(height_feet, height_inches)

  bmi = calculate_bmi(weight_kg, height_cm)

  display_bmi(bmi)


if __name__ == "__main__":
  main()

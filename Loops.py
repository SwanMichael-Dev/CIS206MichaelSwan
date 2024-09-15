POUNDS_TO_KG_CONVERSION_FACTOR = 0.453592
FEET_TO_CM_CONVERSION_FACTOR = 30.48
INCHES_TO_CM_CONVERSION_FACTOR = 2.54

def get_user_weight():
  """Gets the user's weight in pounds."""
  while True:
    user_input = input("Enter your weight in pounds: ")
    if user_input.lower() == 'quit':
      exit()  
    try:
      weight_pounds = float(user_input)
      if weight_pounds > 0: 
        return weight_pounds
      else:
        print("Weight must be a positive number. Please try again or type 'quit' to exit.")
    except ValueError:
      print("Invalid weight input. Please enter a number or type 'quit' to exit.")

def get_user_height_feet():
  """Gets the user's height in feet."""
  while True:
    user_input = input("Enter your height in feet: ")
    if user_input.lower() == 'quit':
      exit()  
    try:
      height_feet = int(user_input)
      if height_feet >= 0: 
        return height_feet
      else:
        print("Height in feet must be a non-negative number. Please try again or type 'quit' to exit.")
    except ValueError:
      print("Invalid height (feet) input. Please enter a whole number or type 'quit' to exit.")

def get_user_height_inches():
  """Gets the user's height in inches."""
  while True:
    user_input = input("Enter your height in inches: ")
    if user_input.lower() == 'quit':
      exit()  
    try:
      height_inches = int(user_input)
      if 0 <= height_inches <= 11: 
        return height_inches
      else:
        print("Height in inches must be between 0 and 11. Please try again or type 'quit' to exit.")
    except ValueError:
      print("Invalid height (inches) input. Please enter a whole number or type 'quit' to exit.")


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


def display_bmi_table():
  """Displays a BMI table with height and weight increments."""
  print("BMI Table:")
  print("Height (inches) |", end="")
  for height_inches in range(58, 77, 2):
    print(f"{height_inches: >12}", end=" | ")
  print()
  height_feet = 4 
  for weight_pounds in range(100, 251, 10):
    print(f"{weight_pounds: >13} |", end="")
    for height_inches in range(58, 77, 2):
      weight_kg = convert_weight_to_kg(weight_pounds)
      height_cm = convert_height_to_cm(height_feet, height_inches)
      bmi = calculate_bmi(weight_kg, height_cm)
      print(f"{bmi: >12.1f}", end=" | ")
    print()
  print("-" * 40)


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
  while True:
    user_input = input("Would you like to calculate your BMI? (yes/no): ")
    if user_input == "yes":
      weight_pounds = get_user_weight()
      height_feet = get_user_height_feet()
      height_inches = get_user_height_inches()

      weight_kg = convert_weight_to_kg(weight_pounds)
      height_cm = convert_height_to_cm(height_feet, height_inches)

      bmi = calculate_bmi(weight_kg, height_cm)

      display_bmi(bmi)
      display_bmi_table()
    elif user_input == "no":
      break
    else:
      print("Invalid input. Please enter 'yes' or 'no'.")
if __name__ == "__main__":
  main()
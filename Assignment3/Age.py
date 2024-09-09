def calculate_age(birth_year):
    # Data type validation: Ensure birth year is an integer.
    if not isinstance(birth_year, int):
        raise ValueError("Birth year must be an integer.")

    # Constraint validation: Ensure birth year is within a reasonable range.
    current_year = 2024  
    if birth_year > current_year:
        raise ValueError("Invalid birth year: cannot be in the future.")

    age = current_year - birth_year

    # Nested if statement for age validation
    if age > 0:
        return age
    else:
        raise ValueError("Invalid birth year: must be before the current year.")
if __name__ == "__main__":
    #Exception handling
    try:
        birth_year = int(input("Enter your birth year: "))
        age = calculate_age(birth_year)
        print(f"Your age is: {age}")
    except ValueError as e:
        print(f"Error: {e}")

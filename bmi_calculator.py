# bmi_calculator.py
class BMICalculator:
    """A class for calculating BMI."""

    POUNDS_TO_KG_CONVERSION_FACTOR = 0.453592
    FEET_TO_INCHES_CONVERSION_FACTOR = 12
    INCHES_TO_METERS_CONVERSION_FACTOR = 0.0254

    def __init__(self):
        """Initializes the BMI calculator."""
        pass

    def calculate_bmi_metric(self, weight_kg, height_cm):
        """Calculates BMI using metric units."""
        height_m = height_cm / 100
        return weight_kg / (height_m ** 2)

    def calculate_bmi_us(self, weight_pounds, height_feet, height_inches):
        """Calculates BMI using US units."""
        weight_kg = self._convert_pounds_to_kg(weight_pounds)
        height_inches = self._convert_feet_to_inches(height_feet, height_inches)
        height_m = self._convert_inches_to_meters(height_inches)
        return weight_kg / (height_m ** 2)

    def _convert_pounds_to_kg(self, weight_pounds):
        """Converts weight from pounds to kilograms."""
        return weight_pounds * self.POUNDS_TO_KG_CONVERSION_FACTOR

    def _convert_feet_to_inches(self, height_feet, height_inches):
        """Converts height from feet and inches to inches."""
        return (height_feet * self.FEET_TO_INCHES_CONVERSION_FACTOR) + height_inches

    def _convert_inches_to_meters(self, height_inches):
        """Converts height from inches to meters."""
        return height_inches * self.INCHES_TO_METERS_CONVERSION_FACTOR
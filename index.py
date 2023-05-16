"""Create a function that accepts a measurement value in inches and
returns the equivalent of the measurement value in feet."""

def inches_to_feet(inches):
    feet = round(inches/12)
    return f"{feet}ft"

print(inches_to_feet(95))

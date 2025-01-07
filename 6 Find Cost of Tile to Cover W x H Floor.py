"""
Script based on the projekts found in https://github.com/karan/Projects 
Find Cost of Tile to Cover W x H Floor - 
Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.
"""
import re

def convert_to_cm(value_with_unit):
    """Converts units to cm for uniform calculation."""
    value, unit = value_with_unit
    inch_to_cm = 2.54
    feet_to_cm = 30.48
    meter_to_cm = 100
    
    if unit == "inch":
        return value * inch_to_cm
    elif unit == "feet":
        return value * feet_to_cm
    elif unit == "meter":
        return value * meter_to_cm
    elif unit == "centimeter":
        return value
    else:
        raise ValueError("Unknown unit. Please use one of the following: 'inch', 'feet', 'meter', or 'centimeter'.")

def split_float_and_string(input_str):
    """Splits number and string from input."""
    match = re.match(r'([\d.]+)\s*(\D+)', input_str)
    if match:
        number_part = float(match.group(1))  # Convert the number part to float
        string_part = match.group(2).strip()  # Get the string part and strip spaces
        return [number_part, string_part]
    else:
        raise ValueError("Input format is incorrect. Expected a number followed by a unit (e.g., '12 meter').")

def take_input(prompt):
    """Takes user input, splits it, and converts the unit to cm."""
    while True:
        try:
            user_input = input(f"Please input the {prompt}: ")
            value_with_unit = split_float_and_string(user_input)
            value_in_cm = convert_to_cm(value_with_unit)
            return value_in_cm
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

def main():
    print("This program calculates the number of tiles needed to cover a rectangular floor.")
    print("The unit for the length and width of the floor and tiles can be one of the following:")
    print("'inch', 'feet', 'meter', or 'centimeter'.")
    
    floor_length = take_input("floor length")
    floor_width = take_input("floor width")
    tile_length = take_input("tile length")
    tile_width = take_input("tile width")
    
    floor_area = floor_length * floor_width
    tile_area = tile_length * tile_width
    
    tiles_needed = floor_area / tile_area
    print(f"You will need {tiles_needed} tiles to cover the floor.")

if __name__ == "__main__":
    main()

"""
This module will handle the conversions between radians <--> degrees

Take user input (string) and validate it to make sure it casts correctly into a float for proper converting
The function will print out an appropriate result with the final conversion


"""

import math


def check_for_float():
    is_float = False
    user_input = 0.0

    while not is_float:
        try:
            user_input = float(input("Enter value to convert> "))
            is_float = True

        except ValueError:
            print("\nUnknown value(s) detected, numeric values only.")
            is_float = False

    return user_input


# Convert radians to degrees
def convert_rad_to_deg():
    print("\nCONVERTING RADIANS TO DEGREES")

    user_input = check_for_float()
    rad_to_deg_conversion = user_input * (180 / math.pi)

    print(f"\n{user_input} radians to degrees is: {rad_to_deg_conversion:.2f} degrees")


# Convert degrees to radians
def convert_deg_to_rad():
    print("\nCONVERTING DEGREES TO RADIANS")

    user_input = check_for_float()
    deg_to_rad_conversion = user_input * (math.pi / 180)

    print(f"\n{user_input} degrees to radians is: {deg_to_rad_conversion:.2f} radians")

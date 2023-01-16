import math

"""
This section will handle the conversions between radians <--> degrees

Take user input (string) and validate it to make sure it casts correctly into a float for proper converting
The function will print out an appropriate result with the final conversion


"""


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


"""
This section will handle the refactoring of the completed given code into appropriate functions (at least two)
"""


def calc_retail_price(wholesale, mark_up):
    return wholesale * mark_up


def check_for_negative(wholesale):
    while wholesale < 0:
        print('ERROR: the cost cannot be negative.')
        wholesale = float(input('Enter the correct wholesale cost:'))

    return wholesale


def find_retail_price_for_items():
    # This program calculates retail prices.
    mark_up = 2.5  # The markup percentage
    another = 'y'  # Variable to control the loop.

    # Process one or more items.
    print("\nRETAIL PRICE FOR ITEM CALCULATOR")
    while another == 'y' or another == 'Y':
        # Get the item's wholesale cost.
        wholesale = float(input("\nEnter the item's wholesale cost: "))
        check_for_negative(wholesale)

        retail = calc_retail_price(wholesale, mark_up)

        # Display the retail price.
        print('Retail price: $', format(retail, ',.2f'))

        # Do this again?
        another = input('Do you have another item? (Enter y for yes): ')

"""
Python Functions
This program will explore the use of functions and file modules

Question 1:
Create two functions that convert from radians to degrees (r2d(x)) and from degrees to
radians (d2r(x)) respectively. Save your functions into a separate Python file and import
the file when you write your main program.

Question 2:
Given the complete program, refactor the program to appropriately implement the use of functions

Author: Josh Reginaldo
https://github.com/itmd-413-jreginaldo/Functions
"""

import functions


def main():
    # Question One Solution(s)
    functions.convert_rad_to_deg()
    functions.convert_deg_to_rad()

    # Question Two Solution(s)
    functions.find_retail_price_for_items()


if __name__ == '__main__':
    main()

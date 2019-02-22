"""
===================   TASK 1   ====================
* Name: Can String Be Float
*
* Write a function `can_string_be_float` that will
* check whether the passed string value can be
* converted to float. If the string value can be
* successfully converted to float, function should
* return `True` otherwise it should return `False`.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""


def main():

    user_value = input("Enter string which will be evaluated: ")
    print(can_string_be_float(user_value))
    print(float(user_value))

main()

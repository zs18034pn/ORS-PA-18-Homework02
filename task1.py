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
def can_string_be_float(user_value):

    allowed_characters=['0','1','2','3','4','5','6','7','8','9','.','-']
    for ch in user_value:
        if ch not in allowed_characters:
            return False
        number_of_points = 0
        for ch in user_value:
            if ch == '.':
                number_of_points = number_of_points + 1
        if number_of_points > 1:
            return False
        number_of_minuses = 0
        for ch in user_value:
            if ch=='-':
                number_of_minuses=number_of_minuses + 1
        if number_of_minuses > 1:
            return False
        if number_of_minuses == 1:
            if user_value[0] != '-':
                return False
    return True



def main():

    user_value = input("Enter string which will be evaluated: ")
    if can_string_be_float(user_value):
        print(float(user_value))
    else:
        print("User value can not be float!")

main()

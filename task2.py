"""
===================   TASK 2   ====================
* Name: Convert Kilometers To Miles
*
* Write a script that will convert kilometers to
* miles. Script should ask user for input and check
* if user input is valid. If not, the script should
* quit immediately with appropriate message.
*
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Note: You may use `can_string_be_float` function
* from previous task to validate user input.
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
    user_value= (input("Enter lenght in kilometers: "))
    if can_string_be_float(user_value):
        print("The lenght in miles is: ", float(user_value) * 0.6214)
    else:
        print("Your input is not valid!")

main()
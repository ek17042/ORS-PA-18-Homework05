"""
===================   TASK 3   ====================
* Name: Convert to Octal
*
* Write a function `dec2oct` that will convert
* positive integer number passed as argument into
* the octal based number. 
*
* Note: Please describe in details possible cases
* in which your solution might not work. It is not
* allowed to use built-in functions.
*
* Use main() function to test your solution.
===================================================
"""
def dec2oct(number):
    remainder = ""
    while number > 0:
        whatsleft = number % 8
        remainder += str(whatsleft)
        number = number // 8
    return remainder[-1:: -1]


def main():

    oct_number = dec2oct(11)
    print("The wanted number is: ", oct_number)

main()
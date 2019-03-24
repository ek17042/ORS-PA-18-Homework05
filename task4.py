"""
===================   TASK 4   ====================
* Name: Can String Be Float
*
* Write a script that will take integer number as
* user input and return the product of digits. 
* The script should be able to handle incorrect
* input, as well as the negative integer numbers.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""
try:
    number = int(input("Enter the number: "))
    initialproduct = 1
    while number > 0:
        initialproduct *= number % 10
        number = number // 10
except ValueError:
    print("This program doesn't support the value you entered. Please try again :)")


def main():

    product = initialproduct
    print("The wanted product is: ", product)

main()

#When the input value is negative, the program gives wrong result
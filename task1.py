"""
===================   TASK 1   ====================
* Name: Power to the Number
*
* Write a function `numpower()` that will for the
* passed based number `num` and exponent `expo`
* return the value of the number `num` raised to
* the power of `expo`.
*
* Note: Please describe in details possible cases
* in which your solution might not work. It is not
* allowed to use built-in operators and functions
* for this task.
*
* Use main() function to test your solution.
===================================================
"""
def numpower(num,exp):
    if (exp == 0):
        return (1)
    if (exp == 1):
        return (num)
    if (exp != 1):
        return (num * numpower(num, exp - 1))

def main():

    x = (int(input("Enter the number: ")))
    y = (int(input("Enter the exponent: ")))
    print("The wanted result is:",numpower(x, y))


main()
#This program doesn't work for negative value of exponent
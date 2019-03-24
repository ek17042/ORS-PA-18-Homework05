"""
===================   TASK 5   ====================
* Name: Average Value
*
* Write a function `averageval` that will take a
* integer list as an argument and return the 
* average value of the list elements.  
*
* Note: Please describe in details possible cases
* in which your solution might not work. It is not
* allowed to use built-in functions.
*
* Use main() function to test your solution.
===================================================
"""
def averageval(list):
    sumofelements = 0

    for i in list:
        sumofelements += i
    average = sumofelements / len(list)
    return average


def main():
    averagevalue = averageval([1,6,8,10,124,14,106,18])
    print("The average value of the list elements is:",averagevalue)

main()
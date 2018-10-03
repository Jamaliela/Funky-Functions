######################################################################
# Author: Elaheh Jamali
# Username: Jamalie & Hilljac

# Assignment: T06: Funky Functions
# Purpose:  Practice creating new functions
# Practice using return values from fruitful functions
#
#
######################################################################
# Acknowledgements:
#   Function is Exercise 2 from the CSC textbook
####################################################################################


def day_name(number):
    """
    A function that will convert an integer from 0 to 6 to days of the week

    :param: number: the number that the user wants the day for
    :return: the day of the week that is equivalent to the number
    """
    if number == 0:
        return "Sunday"
    if number == 1:
        return "Monday"
    if number == 2:
        return "Tuesday"
    if number == 3:
        return "Wednesday"
    if number == 4:
        return "Thursday"
    if number == 5:
        return "Friday"
    if number == 6:
        return "Saturday"


def main():
    """
    main function that will call the existing function

    :return: None
    """
    print("we will let you know the day name for each number")
    number = int(input("Type a number from 0 to 6"))
    name = day_name(number)
    print(name)


if __name__ == "__main__":
    main()

######################################################################
# Author: Ela Jamali & Jacob Hill
# Username: jamalie & hilljac
#
# Assignment: T06: Test suite for the other pycharm file
# Purpose:  Uses tests to ensure that our other file works the way it is meant to
#
######################################################################
# Acknowledgements:
#   Author of this code closely followed similar code by Dr. Scott Heggen
#
####################################################################################
import sys

from Jamalie_hilljac_t06 import *


def testit(did_pass):
    """
    Print the result of a unit test.

    :param did_pass: Boolean representing if the unit test passed or failed
    :return: None
    """
    # This function works correctly--it is verbatim from the text, Chapter 6

    linenum = sys._getframe(1).f_lineno                 # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def day_name_suite():
    """
    The test_suite function utilizes the testit() function,
    and is designed to test the day_name function.

    :return: None
    """
    print("\nRunning the day_name_test_suite()).")

    testit(day_name(0) == "Sunday")
    testit(day_name(50) == None)
    testit(day_name(6) == "Saturday")
    testit(day_name(-2) == None)
    testit(day_name(1) == "Monday")
    testit(day_name(3) == "Wednesday")
    testit(day_name(5) == "Friday")
    testit(day_name(2) == "Tuesday")

    print("\nEnding the day_name_test_suite()).")


def main():
    """
    A program that returns a specific number for each day of the week that a user puts in

    :return: None
    """

    day_name_suite()


if __name__ == "__main__":
    main()

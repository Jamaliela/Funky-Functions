######################################################################
# Author: Dr. Scott Heggen      TODO: Change this to your names
# Username: heggens             TODO: Change this to your usernames
#
# Assignment: T06: Funky Functions Test Suite
# Purpose:  Test suite to test the willoughby_wallaby function in t06_funky_functions.py
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import sys

from t06_funky_functions import *


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


def funky_functions_suite():
    """
    The test_suite function utilizes the testit() function,
    and is designed to test the willaby_wallaby() function.

    :return: None
    """
    print("\nRunning the funky_functions_test_suite()).")
    ##########################################
    testit(willoughby_wallaby("Scott") == "Wott")      # Tests consonant blend
    testit(willoughby_wallaby("Felix") == "Welix")     # Tests non-consonant blend
    testit(willoughby_wallaby("Oscar") == "Wscar")     # Tests a case that worked, but is this correct?
    testit(willoughby_wallaby("Isaac") == "Wsaac")     # How about this one?
    testit(willoughby_wallaby("Jo") == "Wo")           # Tests two letters only
    testit(willoughby_wallaby("") == "W")              # Tests weird cases, such as no input. Is this what we really wanted?
    # testit(willoughby_wallaby(555) == "W")             # Tests an input with a type we didn't expect. Bad results?
    # testit(willoughby_wallaby([1,2,3]) == "W")         # Another bad type test... how should we handle cases like this?

    ##########################################
    print("\nEnding the funky_functions_test_suite()).")


def main():
    """
    A fun little program that sings the Willabee Wallabee song.

    :return: None
    """

    funky_functions_suite()


if __name__ == "__main__":
    main()

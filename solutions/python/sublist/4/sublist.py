"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"


def sublist(list_one, list_two):
    
    def is_contained(sub, main):
        n, m = len(sub), len(main)
        return any(main[i:i + n] == sub for i in range(m - n + 1))

    # Calculate status
    is_equal = (list_one == list_two)
    is_sub = is_contained(list_one, list_two)
    is_super = is_contained(list_two, list_one)

    match (is_equal, is_sub, is_super):
        case (True, _, _):
            return EQUAL
        case (_, True, _):
            return SUBLIST
        case (_, _, True):
            return SUPERLIST
        case _:
            return UNEQUAL
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
    """checks if sublist"""
    def is_sub(sublists, main):
        n, m = len(sublist), len(main)
        return any(main[i:i + n] == sublists for i in range(m - n + 1))
    
    """The states or possibilities"""
    state = (
        list_one == list_two,
        is_sub(list_one, list_two),
        is_sub(list_two, list_one)
    )

    match state:
        
        case (True, _, _):
            return EQUAL

        case (_, True, _):
            return SUBLIST

        case (_, _, True):
            return SUPERLIST

        case _:
            return UNEQUAL
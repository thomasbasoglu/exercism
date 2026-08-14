"""
This module provides a utility to identify Armstrong (Narcissistic) numbers.
An Armstrong number is a number that is the sum of its own digits each 
raised to the power of the number of digits.
"""

def is_armstrong_number(number):
    """
    Determine whether a number is an Armstrong number.
    
    An Armstrong number is a number that is the sum of its own digits 
    each raised to the power of the number of digits.
    
    :param number: The integer to check.
    :return: True if the number is an Armstrong number, False otherwise.
    """
    digits = [int(digit) for digit in str(number)]
    sum_digits = 0
    for digit in digits:
        sum_digits += digit ** len(digits)
    if sum_digits == number:
        return True
    return False
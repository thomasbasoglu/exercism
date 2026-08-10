"""
This module provides a utility to identify Armstrong (Narcissistic) numbers.
An Armstrong number is a number that is the sum of its own digits each 
raised to the power of the number of digits.
"""

def is_armstrong_number(number):
    digits = [int(digit) for digit in str(number)]
    sum_digits = 0
    for digit in digits:
        sum_digits += digit ** len(digits)
    if sum_digits == number:
        return True
    return False
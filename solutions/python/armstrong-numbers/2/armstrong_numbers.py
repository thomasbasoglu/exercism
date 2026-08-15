def is_armstrong_number(number):
    digits = [int(digit) for digit in str(number)]
    sum_digits = 0
    for digit in digits:
        sum_digits += digit ** len(digits)
    if sum_digits == number:
        return True
    return False
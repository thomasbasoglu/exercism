def is_armstrong_number(number):
    digits = [int(digit) for digit in str(number)]
    checkArm = 0
    for digit in digits:
        checkArm += digit ** len(digits)
    if checkArm == number:
        return True
    return False
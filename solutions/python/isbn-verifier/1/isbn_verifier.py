"""This module checks if the isbn is valid""" 
def is_valid(isbn):
    """Function checking if isbn is valid"""
    clean_isbn = isbn.replace("-", "")
    
    if len(clean_isbn) != 10:
        return False
    
    digits = []
    for i, char in enumerate(clean_isbn):
        if char.isdigit():
            digits.append(int(char))
        elif char == 'X' and i == 9:
            digits.append(10)
        else:
            return False
            
    total = sum(digit * (10 - i) for i, digit in enumerate(digits))

    return total % 11 == 0
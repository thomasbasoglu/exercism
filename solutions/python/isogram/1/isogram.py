"""This checks if its a string is an isogram"""
def is_isogram(string):
    string = string.lower()

    letters = []
    for char in string:
        if char.isalpha():
            if char.lower() in letters:
                return False

            letters.append(char.lower())

    return True
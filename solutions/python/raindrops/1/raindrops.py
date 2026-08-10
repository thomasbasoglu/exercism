"""This is the raindrop exercism project"""
def convert(number):
    """This function makes pling plang plong depending on divisibility"""
    response = ""
    if number % 3 == 0:
        response += "Pling"

    if number % 5 == 0:
        response += "Plang"

    if number % 7 == 0:
        response += "Plong"
    
    if not response:
        return str(number)
    
    return response


"""This is bobs responses """
def response(hey_bob):
    """This func contains the responses"""
    if hey_bob.upper() and hey_bob.endswith("?"):
        return "Calm down, I know what I'm doing!"
    if hey_bob.endswith("?"):
        return "Sure"
    if hey_bob.upper():
        return "Whoa, chill out!" 
    if hey_bob == "":
        return "Fine. Be that way!"
    return "Whatever"

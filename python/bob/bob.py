"""This is bobs responses """
def response(hey_bob):
    """This func contains the responses"""
    processed_input = hey_bob.strip()
    is_yelling = processed_input.isupper()
    is_question = processed_input.endswith("?")

    if not processed_input:
        return "Fine. Be that way!"
    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    if is_question:
        return "Sure."
    if is_yelling:
        return "Whoa, chill out!" 

    return "Whatever."

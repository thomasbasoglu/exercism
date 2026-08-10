"""This function classifies numbers perfect abundant and deficient"""
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")  
    number = int(number)
    aliquot_sum = 0
    for index in range(1, number):
        if number % index == 0:
            aliquot_sum+=index
    if number == aliquot_sum:
        return "perfect"
    if number < aliquot_sum:
        return "abundant"
    if number > aliquot_sum:
        return "deficient"
    

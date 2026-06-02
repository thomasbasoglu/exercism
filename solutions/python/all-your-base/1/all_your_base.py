def rebase(input_base, digits, output_base):
    if input_base < 2: raise ValueError("input base must be >= 2")
    if output_base < 2: raise ValueError("output base must be >= 2")
    
    def to_decimal(digits, base):
        value = 0
        for digit in digits:
            value = value * base + digit

        return value

    def from_decimal(value, base):
        if value == 0:
            return [0]

        digits = []
        while value > 0:
            digits.insert(0, value % base)
            value = value // base
        return digits

    for digit in digits:
        if not (0 <= digit < input_base):
            raise ValueError("all digits must satisfy 0 <= d < input base")

    decimal_value = to_decimal(digits, input_base)
    return from_decimal(decimal_value, output_base)
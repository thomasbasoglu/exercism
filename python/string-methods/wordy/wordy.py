def answer(question):
    q = question.replace("What is", "").replace("?", "").strip()

    if not q:
        raise ValueError("syntax error")

    tokens = q.split()

    def is_int(x):
        try:
            int(x)
            return True
        except ValueError:
            return False

    # First token MUST be number
    if not is_int(tokens[0]):
        raise ValueError("syntax error")

    result = int(tokens[0])
    i = 1
    expect_number = False
    op = None

    while i < len(tokens):
        token = tokens[i]

        if token == "by":
            i += 1
            continue

        if expect_number:
            if not is_int(token):
                raise ValueError("syntax error")

            n = int(token)
            if op == "plus":
                result += n
            elif op == "minus":
                result -= n
            elif op == "multiplied":
                result *= n
            elif op == "divided":
                result //= n

            expect_number = False
            i += 1
        else:
            if token in ["plus", "minus", "multiplied", "divided"]:
                op = token
                expect_number = True
                i += 1
            else:
                if is_int(token):
                    raise ValueError("syntax error")
                else:
                    raise ValueError("unknown operation")

    if expect_number:
        raise ValueError("syntax error")

    return result
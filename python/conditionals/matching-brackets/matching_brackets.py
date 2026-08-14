def is_paired(input_string):
    bracket_map = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in input_string:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack.pop() != bracket_map[char]:
                return False
    
    return len(stack) == 0

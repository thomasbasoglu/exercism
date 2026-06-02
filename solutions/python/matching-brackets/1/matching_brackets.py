def is_paired(input_string):
    # Dictionary to map closing brackets to their corresponding opening ones
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in input_string:
        # Only process bracket characters
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            # If stack is empty or the top doesn't match the required opener
            if not stack or stack.pop() != bracket_map[char]:
                return False
    
    # If the stack is empty, everything was matched correctly
    return len(stack) == 0

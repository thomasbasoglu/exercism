def encode(plain_text):
    encoded_chars = []
    
    # Process each character
    for char in plain_text.lower():
        if char.isdigit():
            encoded_chars.append(char)
        elif char.isalpha():
            # Calculate the mirrored letter
            mirrored_char = chr(ord("z") - (ord(char) - ord("a")))
            encoded_chars.append(mirrored_char)
            
    full_string = "".join(encoded_chars)
    
    # Create groups of 5
    groups = []
    for i in range(0, len(full_string), 5):
        groups.append(full_string[i : i + 5])
        
    return " ".join(groups)

def decode(ciphered_text):
    # Ensure parameter name matches what is used in the loop
    decoded_chars = []
    
    # Loop over the parameter provided to the function
    for char in ciphered_text:
        if char.isdigit():
            decoded_chars.append(char)
        elif char.isalpha():
            # Use the same mirroring logic
            mirrored_char = chr(ord("z") - (ord(char) - ord("a")))
            decoded_chars.append(mirrored_char)
            
    return "".join(decoded_chars)
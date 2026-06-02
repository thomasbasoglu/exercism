def rotate(text, key):
    decrypted = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            
            zero_based_index = ord(char) - base
            
            shifted_index = zero_based_index + key
            
            wrapped_index = shifted_index % 26
            
            new_char_code = wrapped_index + base
            encrypted_char = chr(new_char_code)
            
            decrypted += encrypted_char
        else:
            decrypted += char
            
    return decrypted


def custom_hash(input_string):
    # Initialize the hash value to 0
    hash_value = 0
    
    # Iterate through each character in the input string
    for char in input_string:
        # Update the hash value using the ASCII value of the character
        hash_value = (hash_value * 31 + ord(char)) % (2**32)
    
    return hash_value
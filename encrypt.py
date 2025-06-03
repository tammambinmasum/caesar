def caesar_cipher(text, key, mode):
    """
    Encrypts or decrypts a message using the Caesar cipher.

    Args:
        text (str): The input string to encrypt or decrypt.
        key (int): The shift value (an integer).
        mode (str): 'encrypt' for encryption, 'decrypt' for decryption.

    Returns:
        str: The encrypted or decrypted string.
    """
    result = ""
    
    if mode == 'decrypt':
        key = -key  # Reverse the key for decryption

    for char in text:
        if 'a' <= char <= 'z':
            start = ord('a')
            shifted_char_code = (ord(char) - start + key) % 26 + start
            result += chr(shifted_char_code)

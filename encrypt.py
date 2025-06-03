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

        elif 'A' <= char <= 'Z':
            start = ord('A')
            shifted_char_code = (ord(char) - start + key) % 26 + start
            result += chr(shifted_char_code)
        else:
            result += char  # Keep non-alphabetic characters as they are
            
    return result

def main():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt? (q to quit): ").lower()
        if choice == 'q':
            break
        elif choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' or 'd'.")
            continue

        message = input("Enter your message: ")
        
        while True:
            try:
                key = int(input("Enter the key (an integer): "))
                break
            except ValueError:
                print("Invalid key. Please enter an integer.")

        if choice == 'e':
            encrypted_message = caesar_cipher(message, key, 'encrypt')
            print(f"Encrypted message: {encrypted_message}")
        elif choice == 'd':
            decrypted_message = caesar_cipher(message, key, 'decrypt')
            print(f"Decrypted message: {decrypted_message}")
        print("-" * 30)

if __name__ == "__main__":
    main()

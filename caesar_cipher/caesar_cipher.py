import string
import sys

letters_lowercase = string.ascii_lowercase
letters_uppercase = string.ascii_uppercase

def encrypt(plaintext, shift):
    """
    Encrypts a plaintext message using a Caesar cipher.
    
    Args:
        plaintext (str): The message to be encrypted.
        shift (int): The shift value for the Caesar cipher (1-26).
        
    Returns:
        str: The encrypted message.
    """
    result = ''
    for letter in plaintext:
        if letter.islower():
            index = letters_lowercase.find(letter)
            # wrap around the range of alphabets
            new_index = (index + shift) % 26
            # accumulate encrypted message
            result += letters_lowercase[new_index]
        elif letter.isupper():
            index = letters_uppercase.find(letter)
            new_index = (index + shift) % 26
            result += letters_uppercase[new_index]
        else:
            result += letter
    return result

def decrypt(cipherText, shift):
    """
    Decrypts a ciphertext message using a Caesar cipher.
    
    Args:
        cipherText (str): The message to be decrypted.
        shift (int): The shift value used for the Caesar cipher (1-26).
        
    Returns:
        str: The decrypted message.
    """
    result = ''
    for letter in cipherText:
        if letter.islower():
            index = letters_lowercase.find(letter)
            # wrap around the range of alphabets
            new_index = (index - shift) % 26
            # accumulate decrypted message
            result += letters_lowercase[new_index]
        elif letter.isupper():
            index = letters_uppercase.find(letter)
            new_index = (index - shift) % 26
            result += letters_uppercase[new_index]
        else:
            result += letter
    return result

def main():
    """
    Main function to run the Caesar cipher program.
    
    prompts the user to input a message, a shift value, and an operation (encryption or decryption).
    Validates the inputs and performs the requested operation, then prints the result.
    """
    print("Caesar Cipher\n")
    input_message = input("Enter input message: ")
    shift_value = input("Enter a shift value (1 to 26): ")
   
    # Input validation
    try:
        shift_value = int(shift_value)
    except ValueError:
        print("Shift key should be an integer!")
        sys.exit()

    if shift_value < 1 or shift_value > 26:
        print("Shift key should be between 1 and 26!")
        sys.exit()

    print("\nWhat operation do you want to perform?")
    operation = input("Encryption -> 1, Decryption -> 2: ")
    
    # Input validation
    try:
        operation = int(operation)
    except ValueError:
        print("Option entered is not a number!")
        sys.exit()

    if operation != 1 and operation != 2:
        print("Invalid operation option entered!")
        sys.exit()
        
    if operation == 1:
        result = encrypt(input_message, shift_value)
        operation_name = "encrypted"
    else:
        result = decrypt(input_message, shift_value)
        operation_name = "decrypted"
    
    print(f"The {operation_name} message is: {result}")
        
if __name__ == "__main__":
    main()
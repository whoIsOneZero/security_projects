import string
import sys
from gooey import Gooey, GooeyParser

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

@Gooey(program_name="Caesar Cipher",
       program_description="Caesar cipher encryption and decryption")
def main():
    """
    Main function to run the Caesar cipher program with a GUI.
    
    Uses Gooey to create a graphical user interface for the user to input the message, 
    shift value, and operation type (Encrypt or Decrypt).
    """
    parser = GooeyParser()
    
    parser.add_argument('input_message', help='Enter input message')
    parser.add_argument('shift_value', type=int, help='Enter a shift value (1 to 26)', choices=range(1, 26))
    parser.add_argument('operation', choices=['Encrypt', 'Decrypt'], help='Choose operation')
    
    args = parser.parse_args()
    
    input_message = args.input_message
    shift_value = args.shift_value
    operation = args.operation
        
    if operation == 'Encrypt':
        result = encrypt(input_message, shift_value)
        operation_name = "encrypted"
    else:
        result = decrypt(input_message, shift_value)
        operation_name = "decrypted"
    
    print(f"The {operation_name} message is: {result}")
        
if __name__ == "__main__":
    main()
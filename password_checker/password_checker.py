from gooey import Gooey, GooeyParser

@Gooey(program_name="Password complexity checker", 
       program_description="A tool that assess the strength of a password")
def main():
    """
    Main function that sets up the GUI for the Password Complexity Checker.
    It parses the input password and evaluates its strength.
    """
    parser = GooeyParser()
    
    parser.add_argument(
        'password',
        help='Enter a password:',
        widget='PasswordField'
    )
    
    args = parser.parse_args()
    password = args.password
    
    strength, classification = check_password(password)
    print(f"Password strength: {strength}%, Classification: {classification}")

def check_password(password):
    """
    Evaluates the strength of a given password based on various criteria.
    
    Args:
        password (str): The password to be evaluated.
        
    Returns:
        tuple: A tuple containing the strength percentage and classification.
    """
    length_score, special_char_score, = 0, 0
    upper_score, lower_score, digit_score = 0, 0, 0
    special_chars = "!@#$%^&*()-_=+[{]}|;:'\",<.>/?"
     
    length = len(password)
    
    # special characters
    if len(password) > 12:
        length_score = 30
    elif length >= 8:
        length_score = 20
    else:
        length_score = 10
        
    # special characters
    if any(char in special_chars for char in password):
        special_char_score = 20
        
    # uppercase characters
    if any(char.isupper() for char in password):
        upper_score = 15
    
    # lowercase characters    
    if any(char.islower() for char in password):
        lower_score = 15
    
    # lowercase characters    
    if any(char.isdigit() for char in password):
        digit_score = 20
        
    strength = length_score + special_char_score + upper_score + lower_score + digit_score

    # Classify strength
    if strength >= 80:
        classification = "strong"
    elif 60 <= strength < 80:
        classification = "moderately strong"
    else:
        classification = "weak"

    return strength, classification

if __name__ == "__main__":
    main()
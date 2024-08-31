# random_data_generator.py
import random
import string

def generate_random_string(length=10, include_special_chars=False):
    """
    Generate a random string of specified length.
    
    :param length: Length of the string
    :param include_special_chars: Whether to include special characters
    :return: Randomly generated string
    """
    characters = string.ascii_letters + (string.digits if not include_special_chars else string.punctuation)
    return ''.join(random.choice(characters) for _ in range(length))

def generate_random_number(length=5):
    """
    Generate a random number of specified length.
    
    :param length: Length of the number
    :return: Randomly generated number
    """
    return ''.join(random.choice(string.digits) for _ in range(length))

def generate_random_email():
    """
    Generate a random email address.
    
    :return: Randomly generated email address
    """
    return f"{generate_random_string(8)}@example.com"

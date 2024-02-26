def is_palindrome(s):
    """
    Check if a string is a palindrome.
    
    :param s: The string to check.
    :return: True if the string is a palindrome, False otherwise.
    """
    # Convert the string to lowercase and remove non-alphanumeric characters
    s = ''.join(char.lower() for char in s if char.isalnum())
    # Compare the string with its reverse
    return s == s[::-1]

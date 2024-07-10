import string

def isPalindrome(s: str) -> bool:
    validate_array = s.translate(str.maketrans('', '', string.punctuation + ' ')).lower()
    return validate_array == validate_array[::-1]


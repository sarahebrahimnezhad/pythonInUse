import re

def real_numbers(numbers):
    """
    Checks whether each string in the input list is a valid real number.

    Rules:
    - Can contain a decimal part, an exponent (e or E), or both.
    - If decimal exists, there must be digits on both sides (e.g., 3.5 is valid, 3. is invalid).
    - Exponent cannot contain decimals.
    - Optional + or - is allowed at the beginning of the number and exponent.
    - Spaces are allowed before/after the number, but NOT inside it.
    
    Returns:
    A list of "LEGAL" or "ILLEGAL" for each input string.
    """

    # Regex pattern for a valid real number
    pattern = r"^\s*[+-]?(\d+(\.\d+)?)([eE][+-]?\d+)?\s*$"

    results = []

    # Check each string in the list
    for x in numbers:
        if re.match(pattern, x):
            results.append("LEGAL")
        else:
            results.append("ILLEGAL")

    return results

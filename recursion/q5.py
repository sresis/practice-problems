def return_reversed_string(s):
    """Reverse string recursively."""
    if len(s) <= 1:
        return s[0]

    return return_reversed_string(s[1:]) + return_reversed_string(s[0])
print(return_reversed_string('hello'))
# O(N)
import unittest


def is_substring(string, substring):
    """Checks if it is a substring of a string."""
    return substring in string

def string_rotation(str1, str2):
    """Checks if str2 is a rotation of str1 using only one call of is_substring."""
    if len(str1) == len(str2):
        return is_substring(str1+str1, str2)
    return False

print(is_substring('football', 'ball'))

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = string_rotation(s1, s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
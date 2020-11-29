# O(N)
import unittest


def string_compression(string):
    """basic string compression using counts of repeated characters."""
    # stack to store recent characters
    stack = []
    new_str = ''
    for i in range(len(string)):
        if i == 0:
            stack.append(string[i])
        elif string[i] == stack[-1]:
            stack.append(string[i])
        else:
            new_str += stack[-1] + str(len(stack) )
            stack = [string[i]]
    # see what is left in stack
    new_str += stack[-1] + str(len(stack))
    
    if len(new_str) > len(string):
        return string
    else:
        return new_str
        




class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
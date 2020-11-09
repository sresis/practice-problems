"""
1.
Input: 'USA'
Output: True

2. 
Input: 'Test'
Output: True


3. 
Input: 'hello'
Output: True

4.
Input: 'GREaT'
Output: False

5.
Input: 'GOOd'
Output: False



- if the first letter is upper
- the next letters need to be either all upper or all lower
- if the first letter is lower, the next letters need to be all lower
- if length is 1, return True
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        if word[0].isupper():
            if word[1:].isupper() or word[1:].islower():
                return True
        else:
            if word[1:].islower():
                return True
        return False
        
        
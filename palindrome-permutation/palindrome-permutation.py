import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # for it to be palindrome, all letter counts must be even except up to 1
        odd_count = 0
        letters = Counter(s)
        for letter in letters:
            if odd_count > 1:
                return False
            if letters[letter] % 2 != 0:
                odd_count += 1
        if odd_count > 1:
            return False
        else:
            return True
        
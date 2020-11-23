class Solution:
    def isPalindrome(self, s: str) -> bool:
        # get rid of symbols and spaces
        new_word = ''
        for item in s:
            if item.isalnum():
                new_word += item.lower()
        print(new_word)
        if new_word[::-1] == new_word:
            return True
        else:
            return False
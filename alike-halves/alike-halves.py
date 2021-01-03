class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')
        length = len(s)
        mid = int(length / 2)
        h1 = s[:mid]
        h2 = s[mid:]
        # count vowels in each half
        h1_count = 0
        for char in h1:
            if char in vowels:
                h1_count += 1
        h2_count = 0
        for char in h2:
            if char in vowels:
                h2_count += 1
        return h1_count == h2_count
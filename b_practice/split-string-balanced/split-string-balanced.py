def balancedStringSplit(self, s: str) -> int:
        l_count = 0
        r_count = 0
        pairs = 0
        for char in s:
            if char == 'L':
                l_count += 1
                if l_count == r_count:
                    pairs += 1
            else:
                r_count += 1
                if r_count == l_count:
                    pairs += 1
                    
        return pairs
        
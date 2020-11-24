class Solution:
    def romanToInt(self, s: str) -> int:
        num_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        #Rules: IV = 4, IX = 9, XL = 40, XC = 90, CD = 400, CM = 900  
        final = 0
        for i in range(len(s)):
            if i == 0:
                final += num_dict[s[i]]
            elif num_dict[s[i]] <= num_dict[s[i-1]]:
                final += num_dict[s[i]]
            else:
                final += num_dict[s[i]] - 2 * num_dict[s[i-1]]
        return final
            
        
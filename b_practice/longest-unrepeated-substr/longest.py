class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        char_dict = {}
        left_idx = 0
        for i in range(len(s)):
            # when it is a duplicate
            if s[i] in char_dict and left_idx <= char_dict[s[i]]:
                left_idx = char_dict[s[i]] + 1
            else:
                max_length = max(max_length, i - left_idx + 1)
            char_dict[s[i]] = i
        return max_length
            
            
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # make dict of indexes for each
        letter_dict = {}
        for i in range(len(pattern)):
            if pattern[i] in letter_dict:
                letter_dict[pattern[i]].append(i)
            else:
                letter_dict[pattern[i]] = [i]
        word_dict = {}
        words = s.split(' ')
        for i in range(len(words)):
            if words[i] in word_dict:
                word_dict[words[i]].append(i)
            else:
                word_dict[words[i]] = [i]
        word_vals = []
        letter_vals = []
        for item in word_dict:
            word_vals.append(word_dict[item])
        for item in letter_dict:
            letter_vals.append(letter_dict[item])
        return letter_vals == word_vals
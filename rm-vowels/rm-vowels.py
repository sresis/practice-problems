class Solution:
    def removeVowels(self, S: str) -> str:
        new_str = ''
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i in range(len(S)):
            if S[i] in vowels:
                pass
            else:
                new_str += S[i]
                
        return new_str
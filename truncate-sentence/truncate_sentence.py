class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        array = s.split(' ')
        if k <= len(array):
            array = array[:k]
        final = (' ').join(array)
        return final

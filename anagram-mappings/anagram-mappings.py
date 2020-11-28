class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        output = []
        for item in A:
            output.append(B.index(item))
        return output
            
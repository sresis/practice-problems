class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alts = [0]
        cum_alt = 0
        for i in range(len(gain)):
            cum_alt += gain[i]
            alts.append(cum_alt)
        return max(alts)
        
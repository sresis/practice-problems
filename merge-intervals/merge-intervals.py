class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # handle 1 interval
        if len(intervals) <= 1:
            return intervals
        output = []
        # sort the intervals
        intervals.sort()

        curr = intervals[0]
        for i in range(1,len(intervals)):
            print(curr)
            if intervals[i][0] <= curr[1]:
                curr[1] = max(intervals[i][1], curr[1])
            else:
                output.append(curr)
                curr = intervals[i]
        #handle at end
        if curr not in output:
            output.append(curr)
        return output
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # store starts and ends
        starts = []
        ends = []
        for interval in intervals:
            starts.append(interval[0])
            ends.append(interval[1])
        starts.sort()
        ends.sort()
        s = e = 0
        room_count = available = 0
        while s < len(starts):
            if starts[s] < ends[e]:
                if available == 0:
                    room_count += 1
                else:
                    available -= 1
                s += 1
            else:
                available += 1
                e += 1
        return room_count
                
               
                
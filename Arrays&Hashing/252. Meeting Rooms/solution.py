class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda i : i[0])
        for i in range(1, len(intervals)):
            prevEnd = intervals[i - 1][1]
            if prevEnd > intervals[i][0]:
                return False
        return True

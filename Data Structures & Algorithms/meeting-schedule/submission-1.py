"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        if not intervals:
            return True

        prevMeeting = intervals[0].end
        for meeting in intervals[1:]:
            if meeting.start < prevMeeting:
                return False
            else:
                prevMeeting = meeting.end
        return True
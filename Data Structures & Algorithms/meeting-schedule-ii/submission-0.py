"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        rooms = 1

        if not intervals:
            return 0

        prevMeeting = intervals[0]
        for meeting in intervals[1:]:
            if meeting.start < prevMeeting.end:
                rooms += 1
                if meeting.end < prevMeeting.end:
                    prevMeeting.end = meeting.end
            else:
                prevMeeting.end = meeting.end
        return rooms
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        interval = intervals[0]
        res = []

        for i in range(1, len(intervals)):
            if interval[1] < intervals[i][0]:
                res.append(interval)
                return res + intervals[i:]
            elif interval[0] <= intervals[i][0] <= interval[1] <= intervals[i][1]:
                interval[1] = intervals[i][1]
            elif intervals[i][0] < interval[0]:
                interval[0] = intervals[i][0]
            elif interval[0] <= intervals[i][0] and intervals[i][1] <= interval[1]:
                continue
            else:
                res.append(interval)
                interval = intervals[i]
        
        res.append(interval)
        return res
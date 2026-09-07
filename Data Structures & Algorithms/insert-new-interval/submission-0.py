class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        # 3 conditions
        #

        for i in range(len(intervals)):
            # if the newInterval ends before the current interval starts
            if newInterval[1] < intervals[i][0]:
                return res + [newInterval] + intervals[i: ]
            # if the newInterval starts
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # if the newInterval overlap with the current interval
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
            
        res.append(newInterval)
        return res
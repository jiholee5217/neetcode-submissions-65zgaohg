class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort each interval in intervals by the first element of their array
        intervals.sort(key = lambda interval: interval[0])

        # create a merged array
        merged = []

        # loop through all the interval in intervals
        for interval in intervals:
            # and if merged array is empty or if the second element of the last element in merged is
            # less than the first element of current interval, just append the current interval to 
            # merged array
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            # else leave the first element of the the last array in the merged the same and change the
            # second element to the max of the second element of the last array in merged or second element
            # of the current interval
            else:
                merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]

        return merged

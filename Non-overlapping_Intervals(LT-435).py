class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if not intervals:
           return 0
        intervals.sort(key = lambda x:x[1])
        noI=0
        prev_end = intervals[0][1]

        for i in range(1,n):
            if(intervals[i][0] < prev_end):
                noI+=1
            else:
                prev_end = intervals[i][1] 

        return noI            
         
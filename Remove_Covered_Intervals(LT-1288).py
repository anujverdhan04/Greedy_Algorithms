class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x:(x[0], -x[1]))

        prev = 0
        count = 0
        for interval in intervals:
            if(interval[1] > prev):
                count +=1
                prev = interval[1]
        return count        



            
        
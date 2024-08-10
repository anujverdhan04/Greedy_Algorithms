class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
      
        n = len(intervals)
        result = []
        i =0
        # To check the left side portion
        while(i<n and intervals[i][1] < newInterval[0]):
            result.append(intervals[i])
            i+=1
        # To check thee right side portion    
        while(i<n and intervals[i][0] <= newInterval[1]):
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1] , intervals[i][1])
            i+=1
        result.append(newInterval)
        while(i<n):
            result.append(intervals[i])
            i+=1
        return result    

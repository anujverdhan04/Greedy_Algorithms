class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in index_map:
                if (i-index_map[nums[i]]) <=k:
                    return True
            index_map[nums[i]] = i
        return False        


'''
        pairs = []
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and abs(i - j )<= k:
                    return True    
            return False            
 '''       
        
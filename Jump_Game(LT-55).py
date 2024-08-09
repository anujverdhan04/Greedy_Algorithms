class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0
        for i in range(len(nums)):
            if i > max_index:
                return False
            max_index = max(max_index, i + nums[i])
        return True

'''        
        n = len(nums)
        for i in range(n):
            nums.sort()
            if(nums[i] ==0 and i< n-1):
                return False
        if(nums[i] !=0):
            return True        
'''
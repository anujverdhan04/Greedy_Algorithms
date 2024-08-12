class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        unique_positive_numbers = set(num for num in nums if num > 0)
        return len(unique_positive_numbers)

'''        
        count = 0
        while any(nums):
            smallest_number = min(nums)  
            for i in range(len(nums)):
                if nums[i] > 0:  # Only subtract from non-zero elements
                    nums[i] -= smallest_number
            count += 1  # Increment operation count
        
        return count
'''        
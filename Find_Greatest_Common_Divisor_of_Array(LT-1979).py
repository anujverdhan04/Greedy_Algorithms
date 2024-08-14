class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maxi = max(nums)
        mini = min(nums)
        while mini != 0:
            maxi, mini = mini, maxi % mini
        
        return maxi
        
'''
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        return gcd(maxi, mini)


        maxi = max(nums)
        mini = min(nums)
        for num in nums:
            if(maxi %mini !=0 and mini%2 !=0):
                return 1
            elif(maxi %mini !=0 and mini%2 ==0):
                return 1    
            else:
                return mini    
'''
        
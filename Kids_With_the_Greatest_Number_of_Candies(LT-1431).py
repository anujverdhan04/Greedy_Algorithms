class Solution:
    def kidsWithCandies(self, candies: List[int], eC: int) -> List[bool]:
        
        maxi = max(candies)
        result =[]
        for candy in candies:
            if candy+ eC >= maxi:
                result.append(True)
            else:
                result.append(False) 
        return result
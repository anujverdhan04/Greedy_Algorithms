class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
         res = 0
         while any(grid):
            max_values = []
            for row in grid:
                if row:
                    max_digit = max(row)
                    row.remove(max_digit)
                    max_values.append(max_digit)

            if max_values:
                    res += max(max_values)
         return res        

'''
     res = 0
        for row in grid:
            if row:
                max_digit = max(row)
                row.remove(max_digit)
                res += max_digit
        return res 
'''        

        
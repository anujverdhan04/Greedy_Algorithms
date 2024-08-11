class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = [0]*n
        index_map = {}
        for i in range(n):
            if arr[i] not in index_map:
                index_map[arr[i]] = []
            index_map[arr[i]].append(i)
        for indices in index_map.values():
           for i in indices:
                total_distance = 0
                for j in indices:
                    total_distance += abs(i - j)
                result[i] = total_distance
        return result
                

'''
        for i in range(n):
            for j in range(i+1 , n):
                if(arr[i] == arr[j]):
                    add = abs(i-j)
                    result.append(add)
        return result  
'''


        
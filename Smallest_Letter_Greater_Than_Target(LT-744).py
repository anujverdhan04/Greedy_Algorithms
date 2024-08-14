class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        for letter in letters:
            if letter > target:
                return letter
       
        return letters[0]
'''        
        mini = min(letters)
        
        for letter in letters:
            if( target < mini):
                return mini
            else:    
                return letters[0]    
'''

class Solution:
    def findContentChildren(self, greed: List[int], cookies: List[int]) -> int:
        num_children = len(greed)
        num_cookies = len(cookies)
        child_index = 0
        cookie_index = 0
        
        greed.sort()
        cookies.sort()
        
        while child_index < num_cookies and cookie_index < num_children:
            if greed[cookie_index] <= cookies[child_index]:
                cookie_index += 1
            child_index += 1
            
        return cookie_index
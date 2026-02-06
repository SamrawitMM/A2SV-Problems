from collections import Counter
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}

        for inx, num in enumerate(nums):
            if num in last_seen and inx - last_seen[num] <= k:
                return True
            
            last_seen[num] = inx
        
        return False
        
        

                   
                
        

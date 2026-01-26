class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for num in range(left, right+1):
            found = False
            for l, r in ranges:
                if l <= num <= r:
                    found = True
                    break
            if not found:
                return False

        
        return True

                
                
        


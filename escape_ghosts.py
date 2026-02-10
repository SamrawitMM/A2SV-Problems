class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        x, y = target
        me = [0, 0]
        
        min_step = abs(me[0] - x)  + abs(me[1] - y)
        for i, j in ghosts:
            if abs(x - i) + abs(y - j) <= min_step:
                return False
            
        return True


        

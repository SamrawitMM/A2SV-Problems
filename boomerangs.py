class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        result = 0
        for x1, y1 in points:
            distance_count = {}
            for x2, y2 in points:

                    dx = x1-x2
                    dy = y1-y2

                    d = dx**2 + dy**2
                    distance_count[d] = distance_count.get(d, 0) + 1

            for m in distance_count.values():
                result += m * (m-1)

            
        return result


        

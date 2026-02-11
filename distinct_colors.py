from collections import defaultdict
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        marked_balls = {}
        color_count = defaultdict(int)
        distinct = 0
        result = []

        for ball, color in queries:

            # if the color exists
            if ball in marked_balls:
                old_color = marked_balls[ball]
                color_count[old_color] -= 1
            
                if color_count[old_color] == 0:
                    distinct -= 1

            # if it is a new color
            marked_balls[ball] = color

            if color_count[color] == 0:
                distinct += 1

            color_count[color] += 1

            result.append(distinct)

        return result

            
        

        
                


            
       
                 



        

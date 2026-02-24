class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        record = {}
        for height, name in zip(heights, names):
            record[height] = name

        # selection sort
        for i in range(len(heights)):
            max_index = i
            for j in range(i+1, len(heights)):
                if heights[j] > heights[max_index]:
                    max_index = j
            
            heights[i], heights[max_index] = heights[max_index], heights[i]

        # print(heights)
        
        # # Bubble sort
        # for i in range(len(heights)):
        #     for j in range(len(heights) - 1):
        #         # from bigger to smaller element
        #         if heights[j] < heights[j+1]:
        #             heights[j], heights[j+1] = heights[j+1], heights[j]
     

        # print(heights)
        result = []
        for height in heights:
            print(record[height])
            result.append(record[height])

        return result
            

        




        

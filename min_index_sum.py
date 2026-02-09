class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = { word: inx for inx, word in enumerate(list2)}

        result = []
        min_sum = float('inf')

        for inx, word in enumerate(list1):
            if word in index_map:
                index_sum = inx + index_map[word]

                if index_sum < min_sum:
                    min_sum = index_sum
                    result = [word]
                elif index_sum == min_sum:
                    result.append(word)
            
        return result


        

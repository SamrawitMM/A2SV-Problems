class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
      
        result = []
      
        for row in range(len(image)):
          
            reverse = image[row][::-1]
            flipped = [ 1 - x for x in reverse ]
            result.append(flipped)
          
        return result




        

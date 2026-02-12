class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        rows = len(img)
        cols = len(img[0])

        result = [ [0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):

                count = 0
                total = 0

                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        new_i = i + x
                        new_j = j + y

                        if new_i >= 0 and new_i < rows and new_j >= 0 and  new_j < cols:
                            total += img[new_i][new_j]
                            count += 1

                result[i][j] = total // count

        
        return result



class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1,n+1))
        
        start_index = 0
     
        while len(friends) > 1:
            if start_index + k > len(friends):
                start_index = (start_index + k - 1 ) % len(friends)
            else:
                start_index = start_index + k - 1
            
            del friends[start_index]

        return friends[0]       





        

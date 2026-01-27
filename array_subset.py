#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        
        freq_a = {}
        freq_b = {}
        
        # frequency of array a
        for num in a:
            if num not in freq_a:
                freq_a[num] = 1
            else:
                freq_a[num] += 1
        
        # frequency of array b
        for num in b:
            if num not in freq_b:
                freq_b[num] = 1
            else:
                freq_b[num] += 1
        
        
        for num, inx in freq_b.items():
            if num in freq_a and freq_a[num] < inx:
                return False
            elif num not in freq_a:
                return False
        
        return True

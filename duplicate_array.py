class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = [0] * (len(nums)+1)
        result = []

        for num in nums:
            freq[num] += 1
            if freq[num] == 2:
                result.append(num)

        return result

            
        

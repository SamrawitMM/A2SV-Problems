class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        
        for row in nums:
            row.sort()

        score = 0
        for col in range(len(nums[0])):
            col_max = 0
            for row in range(len(nums)):
                col_max = max(col_max, nums[row][col])
            score += col_max


        return score




class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq_nums = {}
        for num in nums:
            freq_nums[num] = freq_nums.get(num, 0) + 1

        for count in freq_nums.values():
            if count >= 2:
                return True

        return False

        

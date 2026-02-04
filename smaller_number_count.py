from collections import Counter

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq_nums = Counter(nums)

        sorted_freq = sorted(freq_nums)
        smaller_count = {}
        running_total = 0

        for num in sorted_freq:
            smaller_count[num] = running_total
            running_total += freq_nums[num]

        return [smaller_count[num] for num in nums]

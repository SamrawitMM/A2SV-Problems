from bisect import bisect_left
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        sorted_list = []
        result = [0] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            pos = bisect_left(sorted_list, nums[i])
            result[i] = pos
            sorted_list.insert(pos, nums[i])
        
        return result

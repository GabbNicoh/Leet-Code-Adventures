class Solution(object):
    def twoSum(self, nums: list, target: int) -> dict:
        hmap = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hmap:
                return i, hmap[comp]
            hmap[nums[i]] = i
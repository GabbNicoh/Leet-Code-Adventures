class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hmap = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hmap:
                return i, hmap[comp]
            hmap[nums[i]] = i
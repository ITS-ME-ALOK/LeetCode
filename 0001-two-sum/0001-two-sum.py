class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            j = target - num

            if j in seen:
                return [seen[j], i]

            seen[num] = i

        return []


        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
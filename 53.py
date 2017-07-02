class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            raise RuntimeError("Empty nums!")

        g_max = nums[0]
        last_step_max = nums[0]
        for i in range(1, len(nums)):
            max_end_here = max(nums[i], nums[i] + last_step_max)
            g_max = max(g_max, max_end_here)
            last_step_max = max_end_here

        return g_max


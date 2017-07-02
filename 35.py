class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def f(self, nums, target, left, right):
            if left >= right:
                if nums[left] >= target:
                    return left
                elif nums[left] < target:
                    return left + 1
            else:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    return f(self, nums, target, left, mid - 1)
                else:
                    return f(self, nums, target, mid + 1, right)

        return f(self, nums, target, 0, len(nums) - 1)

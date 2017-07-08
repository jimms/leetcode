class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not nums:
            return nums

        input_r = len(nums)
        input_c = len(nums[0])

        if input_r * input_c != r * c:
            return nums

        t = []
        for rr in nums:
            for n in rr:
                t.append(n)

        return [t[i:i+c] for i in range(0, len(t), c)]

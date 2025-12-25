class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_0 = 0
        curr_max = float('-inf')
        for num in nums:
            sum_0 = max(sum_0 + num, num)
            curr_max = max(curr_max, sum_0)
        return max(curr_max, sum_0)
        
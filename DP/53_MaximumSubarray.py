#子数组必须是连续的，子序列不是连续的
#dp怎么定义，dp[i]是指以nums[i]结尾的最大子数组和
#上一个状态基础上，怎么转变，要不就是num本身，要不就是上一个状态加上num
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_len = len(nums)
        dp = {}
        dp[0] = nums[0]
        res = dp[0]
        for i in range(1, num_len):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
            res = max(res, dp[i])
        return res

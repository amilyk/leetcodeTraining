class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #完全背包问题，但返回的组合有重复，比如112 和 121 是2个解答，排列问题
        #dp[target]的组合数
        #排列数量：外循环背包容量，内循环选择物品
        #组合数量（换硬币II）：外循环选择物品，内循环选择背包容量
        dp = [0] * (target+1)
        dp[0] = 1        
        for j in range(1,target+1):
            for i in range(len(nums)):
                if j - nums[i] >= 0:
                    dp[j] += dp[j-nums[i]]
        return dp[target]

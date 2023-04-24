class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        #完全背包问题，硬币数量无限
        #背包问题，外循环都是选择，内循环是状态。零钱I是相反的，内循环是选择
        dp=[0]*(amount+1)
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(amount+1):
                if j - coins[i] >= 0:
                    dp[j] += dp[j-coins[i]]
        return dp[amount]



class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #最少硬币数量
        #dp[amount]
        #dp[i] = min(dp[i-coin])
        
        #取最小，所以dp初始化不能为0，
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i - coin < 0: continue
                #取最小，所以dp初始化不能为0，而是较大的数，肯定小于是金额+1，都用1元硬币
                dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[amount] if dp[amount] != amount+1 else -1
        #小心没有这样的组合的情况，硬币数为-1

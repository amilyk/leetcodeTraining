class Solution(object):
    def maxProfit_method1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        贪心
        """
        profit=0
        for day in range(len(prices)-1):
            if prices[day] < prices[day+1]:
              profit += prices[day+1]-prices[day]
        return profit

    def maxProfit_method2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        status:0不持有,1持有 dp[day][status]收益
        动态规划
        """
        n = len(prices)
        dp = [[0]*2 for i in range(n)]
        dp[0][0],dp[0][1] = 0,-prices[0]
        for day in range(1,n):
            dp[day][0] = max(dp[day-1][0],dp[day-1][1]+prices[day])
            dp[day][1] = max(dp[day-1][1],dp[day-1][0]-prices[day])
        return dp[n-1][0]

if __name__ == '__main__':
    solu = Solution()
    prices=[1,2,3,4,5]
    profit = solu.maxProfit_method2(prices)
    print(profit)


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #子集背包问题
        #把前N个商品，装到容量为Sum(nums)/2的背包里，是否可以装进去(True/False)
        n = len(nums)
        w = sum(nums)
        if w % 2 !=0:#奇数不可能分为2半
            return False
        w = int(w / 2)
        dp = [[False]*(w+1) for _ in range(n+1)]

        for i in range(0, n+1):
            dp[i][0] = True

        for i in range(1, n+1):
            for j in range(1, w+1):
                if j - nums[i-1] >= 0:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][w]

        

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #状态，从走到第i间房前面
        #选择，是否要取钱。如果这间取了，只能去i+2的房，如果这间没取，可以i+1的房
        #dp[start] 从start开始取到最多的钱
        #循环从后往前，因为递归来说，走到最后一间才知道
        #base:dp[n] = 0 ,0 ... n,因为有i+2和i+2间房，dp[n+1]
        n = len(nums)
        dp = [0] * (n+2)
        for i in range(n-1,-1,-1):
            #对于第i间房子来说
            #要不就是从i+1过来的，相邻所以第i间不取
            #要不就是从i+2过来的，不相邻，所以可以取第i间+nums[i]
            dp[i] = max(dp[i+1], dp[i+2]+nums[i])
        return dp[0]

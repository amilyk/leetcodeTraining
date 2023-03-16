import numpy as np
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        #1.dp[i][j]定义为s[i..j]的最长回文子序列
        # s[i][i+1]...[j-1][j]
        #2.状态变更：if s[i] == s[j]: dp[i][j] = dp[i+1][j-1]+2
        #                   else: dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        #3.base状态
        #dp[i][i] = 1, dp[i][j]=0 if i>j，求解dp[0][n-1]
        #4.遍历状态
        # i从n-2到0,j从i+1到n-1
        l = list(s)
        n = len(l)
        dp = np.zeros([n,n])#因为下三角都是0
        for i in range(n):#先初始化，就能解决”b“一个字符n为1，n-1为0进入不了循环
            dp[i][i] = 1
        for i in range(n-2,-1,-1):
            for j in range(i+1, n):#都只有遍历上三角
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return int(dp[0][n-1])

import numpy as np
class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        #dp数组为，dp[i][j]代表s[i..j]作为回文串最小插入次数
        #base case: dp[i][i] = 0,dp[i][j]=0 if i > j
        #状态变更（最优子结构）:if s[i] == s[j]: dp[i][j] = dp[i+1][j-1] 已经是回文，不用插入
        #                               else: dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
        # 遍历方向：i-> n-2 到 0， j-> i+1到n-1（从下到上，从左到右）
        s_list = list(s)
        n = len(s_list)
        dp = np.zeros([n,n])
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
        return int(dp[0][n-1])



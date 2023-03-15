import numpy as np
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        #dp数组定义，dp[i][j],代表以text[0..i-1],text[0...j-1]的公共子序列
        #状态变更：dp[i][j] = dp[i-1][j-1] + 1
        # max(dp[i-1][j],dp[i][j-1]) 不用考虑dp[i-1][j-1]，因为最小
        # base状态：dp[0][..] = 0 dp[..][0]=0 代表空字符串与text间的公共子序列
        # 求解dp[m][n]，遍历方向正常
        l1 = list(text1)
        l2 = list(text2)
        l1_len = len(l1)
        l2_len = len(l2)
        dp=np.zeros([l1_len+1,l2_len+1])
        # print dp
        for i in range(1,l1_len+1):
            for j in range(1,l2_len+1):
                if l1[i-1] == l2[j-1]:#dp[i][j]代表的是str 0..i-1
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return int(dp[l1_len][l2_len])#


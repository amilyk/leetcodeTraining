import numpy as np
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        #一、问题定义：dp[i][j]代表word1[0..i-1]与word2[0...i-1]的编辑距离，比如i（word1）变成j（word2）
        #二、状态变更：if word1[i] == word2[j], dp[i][j] = dp[i-1][j-1]
        #         if word1[i] != word2[j], dp[i][j] = min(dp[i-1][j] + 1 delete,dp[i][j-1] + 1 insert, dp[i-1]dp[j-1]+1 replace)
        # 状态变更里操作都是一步，具体而言：
        # 假设word1和word2分别为b、r，求解编辑距离就是b变成r的最小步数
        # 1.dp[i-1][j]，空->r(上个状态怎么求解,insert r后，r->r，此时加上word1[i]为b，（b）r-> r，delete b)
        # 2.dp[i][j-1]，b->空(上个状态怎么求解,delete b后，''->''，此时加上word2[j]为r，''->''(r)，insert r)
        # 3.dp[i-1][j-1]，空->空(上个状态已经转换好了''->''，此时加上word1[i]为b，word2[j]为r，''(b)->''(r)，b替换成r)
        #三、base状态，dp[0][..] = i, dp[..][0] = i，求解dp[m][n]
        #四、遍历方向：1..m 1..n
        #五、方向只有一个，要不是i-> j(word1 -> word2) ，要不就是j->i(word2-> word1) 
        # 选择i-> j(word1 -> word2)
        l1 = list(word1)
        l2 = list(word2)
        # print l1, l2
        l1_len = len(l1)
        l2_len = len(l2)
        dp=np.zeros([l1_len+1, l2_len+1])#从0也就是空字符串开始
        for i in range(1, l1_len+1):#dp[0][0] = 0
            dp[i][0] = i
        for j in range(1, l2_len+1):
            dp[0][j] = j
        for i in range(1, l1_len+1):
            for j in range(1, l2_len+1):
                if l1[i-1] == l2[j-1]:# string 应该是i-1
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
        return int(dp[l1_len][l2_len])
        

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        leng = len(strs)
        dp = [[[0 for _ in range(n+1)] for _ in range(m+1)] for _ in range(leng+1)]
        for i in range(leng):
            index = i + 1
            zeros = strs[i].count('0')
            ones = strs[i].count('1')
            for j in range(m+1):
                for k in range(n+1):
                    #剩余空间(m,n)判断是否可以装下s[i](zeros, ones)
                    if j >= zeros and k >= ones:
                        dp[index][j][k] = max(dp[index-1][j][k], dp[index-1][j-zeros][k-ones]+1)
                    else:
                        dp[index][j][k] = dp[index-1][j][k]
        return dp[leng][m][n] 


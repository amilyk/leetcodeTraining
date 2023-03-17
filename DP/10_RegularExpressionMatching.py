class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        l_s = list(s)
        l_p = list(p)
        memo = {}
        #dp数组定义，dp[i][j]指的是s[i..]与p[j..]是否匹配
        #求解dp[0][0] 
        #base case跳出递归 if j == n: return i == n,模式p到最后，s是否已经到最后了
        #反之，如果s到最后了，p是否只剩下 字符*这样的偶数串
        #状态变更：1.if s[i] == p[j] & p[i+1] == '*': (看(p[i]*)一起匹配0次还是多次)
                 # dp[i][j+2] (s[i+1]不等于p[i],p[i]*匹配0次)|| dp[i+1][j](匹配多次)
                 #2.if s[i] == p[j]:  dp[i+1][j+1]
                 #3.if s[i] != p[j] & p[i+1] == '*':dp[i][j+2] (p[i]*)匹配0次，可以把p[i]*整个从p模式里去掉 
                 #4. if s[i] != p[j]: return false 不匹配 
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            m = len(l_s)
            n = len(l_p)

            #匹配到最后一个子串的情况
            if j == n:#base case 模式p到最后
                return i == m
            if i == m:#base case 子串s到最后
                if (n - j) % 2 == 1: # 字符*是否偶数个
                    return False
                while j + 1 < n:
                    if l_p[j+1] != '*': # 字符*偶数个基础上，是否是字符*这样的格式
                        return False
                    j += 2
                return True
            res = False
            if l_s[i] == l_p[j] or l_p[j] == '.':
                #判断匹配0次还是多次
                if j < n-1 and l_p[j+1] == '*':
                    res = dp(i, j+2) or dp(i+1, j)
                else:
                    res = dp(i+1, j+1)
            else:
                #不匹配
                if j < n-1 and l_p[j+1] == '*':
                    res = dp(i, j+2)
                else:
                    res = False
            memo[(i, j)] = res
            return res
        return dp(0, 0)



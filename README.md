# leetcodeTraining
the practice of leetcode 

### DP
#### 步骤
1. 定义DP数组dp[i][j]代表，比如s[i..j]的最长回文子串长度
2. base状态（起始，比如dp[0][..]），求解的状态是什么（比如dp[m][n]）
3. 状态变更（最优子问题不是DP独有），若穷举无法解>决，考虑最值动态规划) 比如 dp[i-1][j-1] -> dp[i][j]
4. DP数组遍历方向（一定是从已经状态上推导，定义清楚最后求解的状态）
#### dp数组定义
1. 涉及到一个字符串的时候，一般用dp[i][j]代表该字符串s[i...j]的最长回文子串。
2. 涉及到2个字符串的时候，一般用dp[i][j]代表字符串s[0..i]与p[0..j]的最大公共子序列，有时候是以i或j开头。

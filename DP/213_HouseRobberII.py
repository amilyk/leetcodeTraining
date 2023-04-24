class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #改为环形邻居，意思是第一间房和最后一间房是邻居，所以不能同时取
        #因为环形就变成，从0到n-1的最多金额，到(0,n-2)和(1,n-1)中取最大值，因为0
        #和n-1不能同时
        def robRange(nums, start, end):
            dp_i_1 = 0
            dp_i_2 = 0
            for i in range(start, end+1):
                dp_i = max(dp_i_1, dp_i_2+nums[i])
                dp_i_2 = dp_i_1
                dp_i_1 = dp_i
                # 1.... a  a1 a2 ... 往左移动
                # 2. a  a1 a2 ...
            return dp_i

        n = len(nums)
        if n == 1:
            return nums[0]
        return max(robRange(nums, 0, n-2), robRange(nums, 1, n-1))

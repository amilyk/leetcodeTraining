## 将宽度按最小到大排序，相同宽度的则按长度从大到小。只要比较长度即可（变成1维LIS最长递增子序列）
## 但python中这里hard求解的时候n^2超时TLE,因此用二分（logn），n*logn
class Reversinator(object):
        def __init__(self, obj):
            self.obj = obj
        def __lt__(self, other):
            return other.obj < self.obj
            
class Solution(object):

    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        def findleftPos(target, nums):
            if not nums:
                return 0
            left = 0
            right = len(nums)-1
            while left <= right:
                mid = left + (right - left) / 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        # envelopes.sort(key = lambda x: (x[0], -x[1]))
        envelopes = sorted(envelopes, key=lambda x: (x[0], Reversinator(x[1])))
        heights = [l[1] for l in envelopes]
        # print heights

        # Time Limit Exceeded n^2 改成 nlogn
        # dp={}
        # num_len = len(heights)
        # res = 1
        # for i in range(num_len):
        #     dp[i] = 1
        #     for j in range(0,i):
        #         if heights[j] < heights[i]:
        #             dp[i] = max(dp[i], dp[j]+1)
        #     # print(i,dp[i])
        #     res=max(res, dp[i])
        # print heights
        res = []
        for num in heights:
            pos = findleftPos(num, res)
            # print pos,num,res
            if pos >= len(res):#找不到左边界，说明num比res里的值大
                res.append(num)
            else:#比res小的值，左边界pos应该等于0（右边界小于0）
                res[pos] = num
        return len(res)




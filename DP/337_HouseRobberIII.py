# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.memo = {}
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #因为树比较方便的方式，从上到下遍历，但这样得出结果，必须最后一层才知道。
        #递归，第i层结果，来自于i-i层+i不取，或者i-2层+i取
        if not root:
            return 0
        if root in self.memo:
            return self.memo[root]
        #第i层取，到下下层
        if root.left:
            #为啥不是root.left.left，因为只要root.left不为空，就可以继续遍历，假设rob(root.left.left)是空，直接返回0了
            idoleft = self.rob(root.left.left) + self.rob(root.left.right)
        else:
            idoleft = 0
        if root.right:
            idoright = self.rob(root.right.left) + self.rob(root.right.right)
        else:
            idoright = 0
        ido = root.val + idoleft + idoright
        
        #第i层不取，直接取下层
        inot = self.rob(root.left) + self.rob(root.right)
        res = max(ido, inot)
        self.memo[root] = res
        return res

         

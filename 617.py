# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        if not t2:
            return t1

        n = TreeNode(t1.val + t2.val)

        for subtree in ['left', 'right']:
            t1_s = getattr(t1, subtree)
            t2_s = getattr(t2, subtree)
            if t1_s and t2_s:
                s = self.mergeTrees(t1_s, t2_s)
            elif t1_s:
                s = t1_s
            elif t2_s:
                s = t2_s
            else:
                s = None
            setattr(n, subtree, s)

        return n

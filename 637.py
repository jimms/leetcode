# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def visit(self, root, level):
        if not root:
            return

        if level not in self.levels:
            self.levels[level] = []
            if self.max < level:
                self.max = level
        self.levels[level].append(root.val)

        self.visit(root.left, level + 1)
        self.visit(root.right, level + 1)

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ret = []
        self.levels = {}
        self.max = -1

        if not root:
            return ret
        self.visit(root, 0)

        return [float(sum(self.levels[i])) / len(self.levels[i]) for i in range(self.max + 1)]

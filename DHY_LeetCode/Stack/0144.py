
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            x =[]
            return x
        x = self.preorderTraversal(root.left)
        x.insert(0,root.val)
        if (self.preorderTraversal(root.right) != None):
            x.extend(self.preorderTraversal(root.right))
        return x
# @lc code=end


'''
Accepted
68/68 cases passed (40 ms)
Your runtime beats 66.8 % of python3 submissions
Your memory usage beats 7.14 % of python3 submissions (13.6 MB)
'''
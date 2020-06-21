#
# [94] 二叉树的中序遍历
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        if root == None:
            x =[]
            return x
        x = self.inorderTraversal(root.left) 
        x.append(root.val)
        if (self.inorderTraversal(root.right) != None):
            x.extend(self.inorderTraversal(root.right))
        return x
# @lc code=end

'''
Accepted
68/68 cases passed (40 ms)
Your runtime beats 67.47 % of python3 submissions
Your memory usage beats 7.84 % of python3 submissions (13.6 MB)
'''
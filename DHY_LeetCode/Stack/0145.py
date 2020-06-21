# [145] 二叉树的后序遍历
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            x =[]
            return x
        x = self.postorderTraversal(root.left)
        x.extend(self.postorderTraversal(root.right))
        x.append(root.val)
        return x
# @lc code=end

'''
Accepted
68/68 cases passed (36 ms)
Your runtime beats 85.82 % of python3 submissions
Your memory usage beats 7.41 % of python3 submissions (13.6 MB)

'''
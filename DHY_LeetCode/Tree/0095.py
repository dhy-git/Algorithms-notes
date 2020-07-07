# [95] 不同的二叉搜索树 II
#

'''
    分治法，递归实现
'''
# @lc code=start
# Definition for a binary tree node.

from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        List_node = [i for i in range(1,n+1)]
        def Build_BTrees(l_node: List) ->List[TreeNode]:
            res = []
            if len(l_node) == 1:
                return [TreeNode(val=l_node[0])]
            elif len(l_node) == 0:
                return [None]
            for k in range(len(l_node)):
                for left in (Build_BTrees(l_node[:k])):
                    for right in (Build_BTrees(l_node[k+1:])):
                        node = TreeNode(val = l_node[k], left=left, right= right)
                        res.append(node)
            return res
        if n == 0:
            return []
        return Build_BTrees(List_node)

# @lc code=end

'''
Accepted
9/9 cases passed (76 ms)
Your runtime beats 30.01 % of python3 submissions
Your memory usage beats 12.5 % of python3 submissions (15.7 MB)
'''
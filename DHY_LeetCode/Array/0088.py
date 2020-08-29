
# [88] 合并两个有序数组
#

# @lc code=start
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = m+n-1
        while n>0 and m>0:
            if nums1[m-1] > nums2[n-1]:
                nums1[k] = nums1[m-1]
                m-=1
                k-=1
            else:
                nums1[k] = nums2[n-1]
                n-=1
                k-=1
        while n>0:
            nums1[k] = nums2[n-1]
            n-=1
            k-=1
            


# @lc code=end

'''
Accepted
59/59 cases passed (36 ms)
Your runtime beats 89.45 % of python3 submissions
Your memory usage beats 6.9 % of python3 submissions (13.7 MB)
'''
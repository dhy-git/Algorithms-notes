'''
    快速排序应用实例
'''

# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        quick_sort(nums,0, len(nums)-1)

def quick_sort(l: List[int], p, r) -> None:
    if p<r:
        index = departion(l, p, r)
        quick_sort(l, p, index-1)
        quick_sort(l, index+1, r)

def departion(l: List[int], p, r) -> int:
    i = p
    for j in range(p,r):
        if l[j]<= l[r]: 
            l[i],l[j] = l[j],l[i]
            i+=1
    l[r],l[i] = l[i],l[r]
    return i
        

# @lc code=end

'''
Accepted
87/87 cases passed (36 ms)
Your runtime beats 88.61 % of python3 submissions
Your memory usage beats 8.33 % of python3 submissions (13.5 MB)
'''
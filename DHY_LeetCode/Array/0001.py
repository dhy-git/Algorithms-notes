'''
>>>两数之和:
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

    示例:
    给定 nums = [2, 7, 11, 15], target = 9
    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
'''

'''
解： 哈希表原理查询 target- nums[i]是否存在，时间复杂度O(n)
'''
from typing import List
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        map_num = dict()
        for i in range(l):
            temp = target - nums[i]
            if(temp in map_num):
                return [map_num[temp],i]
            map_num[nums[i]] = i
        
# @lc code=end

'''
29/29 cases passed (56 ms)
Your runtime beats 66.65 % of python3 submissions
Your memory usage beats 6.35 % of python3 submissions (14.8 MB)
'''

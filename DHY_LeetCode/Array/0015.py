
'''
>>>三数之和
    Category	Difficulty	Likes	Dislikes
    algorithms	Medium (24.35%)	1967	-
    给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
    请你找出所有满足条件且不重复的三元组。
    注意：答案中不可以包含重复的三元组。

    示例：
    给定数组 nums = [-1, 0, 1, 2, -1, -4]，
    满足要求的三元组集合为：
    [
    [-1, 0, 1],
    [-1, -1, 2]
    ]
'''

'''
解： 两数之和问题
''' 
from typing import List
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        k = len(nums)
        temp = None
        for i in range(k):
            if(-nums[i] != temp):       #跳过重复元素
                temp = -nums[i]
                new_nums = nums[:]
                new_nums.pop(i)
                #print("nums = ",nums)
                #print("search for",temp, "in", new_nums)
                ret = self.twoSum(new_nums, temp)
                if(ret != None):
                    for each in ret:
                        each.append(nums[i])
                        each = sorted(each)
                        if each not in result:
                            result.append(each)
        #print(result)
        return result
        
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        #print('find',target,'in',nums)
        stack = []
        map_two = dict()
        for i in range(l):
            temp = target - nums[i]
            if(temp in map_two):
                new = [nums[map_two[temp]],nums[i]]
                if new not in stack:
                    stack.append(new)
            map_two[nums[i]] = i
        #print('  result',stack)
        return stack
# @lc code=end

'''
Submission未通过
311/313 cases passed (N/A)
'''

# [781] 森林中的兔子
#

# @lc code=start
from typing import List
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbits_map = dict()
        sum_rab = 0
        for each in answers:
            if each not in rabbits_map:
                rabbits_map[each] = 1
            else:
                rabbits_map[each] += 1
        for each in rabbits_map:
            tmp = 0
            if rabbits_map[each]%(each+1):
                tmp = each+1
            sum_rab += (int(rabbits_map[each] / (each+1))) * (each+1) + tmp
        # print(rabbits_map)
        # print(sum_rab)
        return sum_rab
# l = [1,1,1,1]
# sol = Solution()
# sol.numRabbits(l)

# @lc code=end


'''
Accepted
54/54 cases passed (52 ms)
Your runtime beats 87.5 % of python3 submissions
Your memory usage beats 100 % of python3 submissions (13.7 MB)
'''
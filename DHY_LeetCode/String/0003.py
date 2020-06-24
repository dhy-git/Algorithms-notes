
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = []
        length = 0
        for each in s:
            if each not in queue:
                queue.append(each)
            else:
                length = max(length,len(queue))
                queue = queue[queue.index(each)+1:]
                queue.append(each)
        #处理队列剩余
        length = max(length,len(queue))
        return length
# @lc code=end

'''
Accepted
987/987 cases passed (80 ms)
Your runtime beats 67.29 % of python3 submissions
Your memory usage beats 5.88 % of python3 submissions (13.7 MB)
'''
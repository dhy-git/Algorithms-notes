
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, S: str) -> str:
        i = 0
        s = []
        for i in range(len(S)):
            if len(s) != 0 and s[-1] == S[i]:
                s.pop(-1)
            else:
                s.append(S[i])
        #print(s)
        output = ""
        for each in s:
            output += each
        print(output)
        return output
        
S = "aaaaaaaaa"
sol = Solution()
sol.removeDuplicates(S)
# @lc code=end


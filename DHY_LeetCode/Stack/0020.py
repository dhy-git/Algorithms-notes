'''
>>>有效的括号
Category	Difficulty	Likes	Dislikes
algorithms	Easy (41.37%)	1528	-
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

输入: "{[]}"
输出: true
'''
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        map_s = { ')' : '(',
                  ']' : '[' ,
                  '}' : '{'
                }
        stack_s = []
        for i in range(0,len(s)):
            print(s[i])
            if len(stack_s) == 0:
                stack_s.append(s[i])
            elif s[i] in map_s and stack_s[-1] == map_s[s[i]]:
                stack_s.pop(-1)
            else:
                stack_s.append(s[i])
        if stack_s:
            return False
        else:
            return True
# @lc code=end

'''
Accepted
76/76 cases passed (36 ms)
Your runtime beats 78.5 % of python3 submissions
Your memory usage beats 5.22 % of python3 submissions (13.7 MB)
'''
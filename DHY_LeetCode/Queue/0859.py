'''
>>>亲密字符串
    Category	Difficulty	Likes	Dislikes
    algorithms	Easy (29.06%)	86	-

    给定两个由小写字母构成的字符串 A 和 B ，
    只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；
    否则返回 false 。
    

    示例 1：
    输入： A = "ab", B = "ba"
    输出： true
    示例 2：
    输入： A = "ab", B = "ab"
    输出： false
    示例 3:
    输入： A = "aa", B = "aa"
    输出： true
    示例 4：
    输入： A = "aaaaaaabc", B = "aaaaaaacb"
    输出： true
    示例 5：
    输入： A = "", B = "aa"
    输出： false
    
    提示：
    0 <= A.length <= 20000
    0 <= B.length <= 20000
    A 和 B 仅由小写字母构成。
'''

# @lc code=start
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        #定义队列
        st = []
        if len(A)-len(B):
            return False
        elif A==B:
            for i in range(len(A)):
                for j in range(i+1,len(A)):
                    if A[i] ==A[j]:  
                        return True
            return False
        else:
            for i in range(len(A)):
                if(A[i] != B[i]):
                    #不同入队
                    st.append(i)
        #print(st)
        if(len(st) == 2 and A[st[0]]==B[st[1]] and  A[st[1]]==B[st[0]]):
            return True
        else:
            return False
# @lc code=end

'''
Accepted
23/23 cases passed (36 ms)
Your runtime beats 86.52 % of python3 submissions
Your memory usage beats 100 % of python3 submissions (13.8 MB)
'''
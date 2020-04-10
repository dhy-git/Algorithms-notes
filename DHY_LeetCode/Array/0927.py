'''
>>>三等分
    Category	Difficulty	Likes	Dislikes
    algorithms	Hard (27.79%)	22	-
 
    给定一个由 0 和 1 组成的数组 A，将数组分成 3 个非空的部分，使得所有这些部分表示相同的二进制值。
    如果可以做到，请返回任何 [i, j]，其中 i+1 < j，这样一来：
    A[0], A[1], ..., A[i] 组成第一部分；
    A[i+1], A[i+2], ..., A[j-1] 作为第二部分；
    A[j], A[j+1], ..., A[A.length - 1] 是第三部分。
    这三个部分所表示的二进制值相等。
    如果无法做到，就返回 [-1, -1]。

    注意，在考虑每个部分所表示的二进制时，应当将其看作一个整体。例如，[1,1,0] 表示十进制中的 6，而不会是 3。此外，前导零也是被允许的，所以 [0,1,1] 和 [1,1] 表示相同的值。


    示例 1：
    输入：[1,0,1,0,1]
    输出：[0,3]
    示例 2：
    输出：[1,1,0,1,1]
    输出：[-1,-1]
    
    提示：
    3 <= A.length <= 30000
    A[i] == 0 或 A[i] == 1
'''
# @lc code=start
from typing import List
class Solution:
    def threeEqualParts(self, A: List[int]) -> List[int]:
        count = 0
        load_1 = []
        for i in range(len(A)):
            if A[i] == 1:
                count +=1
                load_1.append(i)        #记录所有A[i]==1的下标i
        #针对全0数组case 的特殊处理，无实际意义
        if count ==0:
            return [0, len(A)-1]
        if count%3 != 0:
            return [-1,-1]
        else:
            #从低位到高位，计算第一个”1“所在位数，即为loda_1三等分基础上的分段偏移，
            bias = len(A)-load_1[count-1]-1
            #分割点下标：
            cut2 = load_1[2*int(count/3)-1] + bias
            cut1 = load_1[int(count/3)-1] +bias
            list_1 = self.pop_zero(A[:cut1+1])
            list_2 = self.pop_zero(A[cut1+1:cut2+1])
            list_3 = self.pop_zero(A[cut2+1:])
            if(list_1 ==list_2 and list_2 ==list_3):
                return [cut1,cut2+1]
            else:
                return [-1,-1]
    #消除二进制数段的高位0
    def pop_zero(self, B: List[int]) -> List[int]: 
        while B:
            if B[0] == 0:
                B.pop(0)
            else:
                return B
            
sol = Solution()
test = [0,0,0,0,0]
print(sol.threeEqualParts(test))

# @lc code=end

'''
Accepted
104/104 cases passed (460 ms)
Your runtime beats 60.76 % of python3 submissions
Your memory usage beats 14.29 % of python3 submissions (15.2 MB)
'''
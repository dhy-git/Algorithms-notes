'''
>>>煎饼排序
    Category	Difficulty	Likes	Dislikes
    algorithms	Medium (63.58%)	39	-

    给定数组 A，我们可以对其进行煎饼翻转：我们选择一些正整数 k <= A.length，
    然后反转 A 的前 k 个元素的顺序。
    我们要执行零次或多次煎饼翻转（按顺序一次接一次地进行）以完成对数组 A 的排序。
    返回能使 A 排序的煎饼翻转操作所对应的 k 值序列。
    任何将数组排序且翻转次数在 10 * A.length 范围内的有效答案都将被判断为正确。

    示例 1：

    输入：[3,2,4,1]
    输出：[4,2,4,3]
    解释：
    我们执行 4 次煎饼翻转，k 值分别为 4，2，4，和 3。
    初始状态 A = [3, 2, 4, 1]
    第一次翻转后 (k=4): A = [1, 4, 2, 3]
    第二次翻转后 (k=2): A = [4, 1, 2, 3]
    第三次翻转后 (k=4): A = [3, 2, 1, 4]
    第四次翻转后 (k=3): A = [1, 2, 3, 4]，此时已完成排序。 
'''
from typing import List
class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        count = 1   #用于排序计数 最大排好则+1
        n =len(A)
        pancake = []
        self.sort_max_n(A, pancake, n)
        return pancake
    #第n大的数归位
    def sort_max_n(self, A: List[int], pancake: List[int], length):
        if length == 1:
            return
        index = A.index(max(A[:length]))
        if index != 0:
            pancake.append(index+1)
            A = self.reverse(A, index+1)
        pancake.append(length)
        A = self.reverse(A, length)
        self.sort_max_n(A,pancake,length-1)


    def reverse(self, A: List[int], n) -> List[int]:
        tmp = []
        for i in range(n):
            tmp.append(A[i])
        for i in range(n):
            A[i] = tmp.pop(-1)
        return A
# @lc code=end
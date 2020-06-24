
# [935] 骑士拨号器
#

# @lc code=start
class Solution:
    def knightDialer(self, N: int) -> int:
        mod = 10**9+7
        #分类
        a = 4   #a: 1 3 7 9
        b = 2   #b: 2 8
        c = 2   #c: 4 6
        d = 1   #d: 0
        if N == 1:
            return 10
        else:
            for i in range(1,N):
                an = (2*b + 2*c) % mod
                cn = (2*d+a) % mod
                #迭代
                b = a
                d = c
                a = an
                c = cn
            return (a+b+c+d) % mod

# @lc code=end

'''
Accepted
120/120 cases passed (160 ms)
Your runtime beats 98.06 % of python3 submissions
Your memory usage beats 100 % of python3 submissions (13.7 MB)
'''
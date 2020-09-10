
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX = 2**31-1
        result = 0
        p = abs(dividend)
        q = abs(divisor)

        # 指数增加 加速逼近
        while(p>=q):
            sum_q = q
            tmp_count = 1
            while(sum_q + sum_q <= p):
                tmp_count += tmp_count
                sum_q += sum_q
            p -= sum_q
            result += tmp_count
        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
            result = 0-result
        if(result>MAX):
            return MAX
        else:
            return result
# @lc code=end


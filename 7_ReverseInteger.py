# 7 Reverse Integer 倒敘 (Easy)  ✓
# Given a 32-bit signed integer, reverse digits of an integer.
''' Input: 123          Input: -123         Input: 120              << 數字倒敘，正負符號不變 >>
    Output: 321         Output: -321        Output: 21  '''

# Note: Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = - 1
        result = int(str(abs(x))[::-1]) # 取正數abs -> 轉成字串str -> 倒敘 -> 轉回整數int型態
        
        if result > 2**31-1:            # 需要再 [−2^31,  2^31 − 1] 範圍內
            return False
        else:
            return sign*result
        # ----------------------------------------------------------------------------------
        # n = x if x > 0 else -x              # n = (x if x > 0) (else -x)
        # res = 0
        # while n:
        #     res = res * 10 + n % 10
        #     n = n // 10 
        # if res > 0x7fffffff:
        #     return 0
        # return res if x > 0 else -res

if __name__ == '__main__':
    a = int(input())
    sol = Solution()
    print(sol.reverse(a))
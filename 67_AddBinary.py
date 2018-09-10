# 67. Add Binary    二進制  (Easy)  ✓ 
# Given two binary strings, return their sum (also a binary string).
# The input strings are both non-empty and contains only characters 1 or 0.
''' Example :                       << 求二進制加法 >>
Input: a = "11", b = "1"        Input: a = "1010", b = "1011"   
Output: "100"                   Output: "10101"                 '''


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a)==0: return b
        if len(b)==0: return a
        if a[-1] == '1' and b[-1] == '1':                                   # .....以 1011,1001 為例 .........
            return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'  # 1011+1001 = str((101+100)+1)+'0'
        if a[-1] == '0' and b[-1] == '0':                                   # 101+100 = str((10+10)+1)+'1'
            return self.addBinary(a[0:-1],b[0:-1])+'0'                      # 10+10 = str(1+1)+'0'
        else:                                                               # 1+1 = str((0)+1)+'0'
            return self.addBinary(a[0:-1],b[0:-1])+'1'                      # => 1011+1001 = 10100
        

if __name__ == '__main__':
    a, b = input(),input()
    sol = Solution()
    print(sol.addBinary(a,b))
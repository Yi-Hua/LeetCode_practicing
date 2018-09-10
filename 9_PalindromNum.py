# 9 Palindrome Number 回文  (Easy)  ✓
# Determine whether an integer is a palindrome. 
# An integer is a palindrome when it reads the same backward as forward.
'''
Input: 121          Input: -121         Input: 10               << 檢測是否為回文(倒敘後不變) >>
Output: true        Output: false       Output: false
'''
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
# Simple Solution----------------------------------------
        return False if x < 0 else int(str(x)[::-1]) == x
# My Answer:---------------------------------------------
        # if x < 0 :                            # 若為負數，False
        #     return False                      
        # num = int(str(abs(x))[::-1])          # 倒敘        
        # if x == num:
        #     return True
        # else: 
        #     return False
            
if __name__ == '__main__':
    n = int(input())
    sol = Solution()
    print(sol.isPalindrome(n))


        


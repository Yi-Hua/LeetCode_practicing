# 66. Plus One  (Easy)  ✓
# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.
''' Example 1:
Input: [1,2,3]                                          Input: [4,3,2,1]
Output: [1,2,4]                                         Output: [4,3,2,2]
Explanation: The array represents the integer 123.      Explanation: The array represents the integer 4321. '''


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # k = digits[-1]
        
        # if k == 9:
        #     digits[-1] = 0
        #     k == digits[-2]
         
        # return digitss = list(map(str, digits))
        k = int(''.join(s))
        l = list(str(k+1))
        l = list(map(int,l))
        return l

        



if __name__ == '__main__':
    s = list(map(int,input().split()))
    sol = Solution()
    print(sol.plusOne(s))

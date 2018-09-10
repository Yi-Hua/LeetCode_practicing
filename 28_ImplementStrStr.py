# 28. Implement strStr()
# Implement strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
''' Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1  '''
# Clarification:
# What should we return when needle is an empty string? This is a great question to ask during an interview.
# For the purpose of this problem, we will return 0 when needle is an empty string. 
# This is consistent to C's strstr() and Java's indexOf().

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        l = len(needle)
        r = -1
        for i in range(len(haystack)):
            if haystack[i:i+l] == needle:
                r = i
                break           #如果沒有break:   input:aaa, WrongAnswer:2, Answer:0
        return r  




if __name__ == '__main__':
    haystack = str(input())
    needle = str(input())
    sol = Solution()
    print(sol.strStr(haystack,needle))
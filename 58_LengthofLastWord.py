# 58. Length of Last Word   (Easy)  ✓
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
# If the last word does not exist, return 0.
# Note: A word is defined as a character sequence consists of non-space characters only.
''' Example: 
Input: "Hello World"
Output: 5               '''

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s.strip() == '':
            return 0
        s = s.split()
        return len(s[-1])


if __name__ == '__main__':
    s = str(input().strip())
    sol = Solution()
    print(sol.lengthOfLastWord(s))

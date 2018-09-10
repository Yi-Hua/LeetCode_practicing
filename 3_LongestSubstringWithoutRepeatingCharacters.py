# 3. Longest Substring Without Repeating Characters 沒有重複字符的最長子串 (Medium) ✓
# Given a string, find the length of the longest substring without repeating characters.
''' Example:            << 找到沒有重複字符的最長子串 >>
Input: "abcabcbb"                       Input: "bbbbb"                      Input: "pwwkew"
Output: 3                               Output: 1                           Output: 3
Explanation: The answer is "abc",       Explanation: The answer is "b",     Explanation: The answer is "wke",
             which the length is 3.                  with the length of 1.  with the length of 3.    

Note that the answer must be a substring, "pwke" is a subsequence and not a substring.  '''

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
       
        dic = {}                        # .....以 abcabcbb 為例...................
        r, x = 0, -1                    # 1) i,k = 0,a --- x = -1, r = 0          dic = {a:0}   
        for i, k in enumerate(s):       # 2) i,k = 1,b --- x = -1, r = 0          dic = {a:0, b:1}            
            if k in dic and x < dic[k]: # 3) i,k = 2,c --- x = -1, r = 0          dic = {a:0, b:1, c:2} 
                x = dic[k]              # 4) i,k = 3,a --- x = 0, r = max{0,3-0}  dic = {a:3, b:1, c:2}   
            r = max(r,i-x)              # 5) i,k = 4,b --- x = 1, r = max{3,4-1}  dic = {a:3, b:4, c:2} 
            dic[k] = i                  # 6) i,k = 5,c --- x = 2, r = max{3,5-2}  dic = {a:3, b:4, c:5} 
        return r                        # 7) i,k = 6,b --- x = 4, r = max{3,6-4}  dic = {a:3, b:6, c:5}
                                        # 8) i,k = 7,b --- x = 6, r = max{3,7-6}  dic = {a:3, b:7, c:5}
                                        # .............................................................        
        # ------------------------------------------------------------------------------------------------
        # start = maxLength = 0
        # usedChar = {}
        
        # for i in range(len(s)):                                 # .....以 abcabcbb 為例...................
        #     if s[i] in usedChar and start <= usedChar[s[i]]:
        #         print(s[i],usedChar[s[i]])
        #         start = usedChar[s[i]] + 1
        #     else:
        #         maxLength = max(maxLength, i - start + 1)

        #     usedChar[s[i]] = i

        # return maxLength




if __name__ == '__main__':
    s = str(input())
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))


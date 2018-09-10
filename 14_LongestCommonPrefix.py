# 14 Longest Common Prefix 最長相同字首 (Easy)  ✓
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
'''
Input: ["flower","flow","flight"]       Input: ["dog","racecar","car"]            << 找出最長的相同字首 >>  
Output: "fl"                            Output: ""
                                        Explanation: There is no common prefix among the input strings.
'''
# Note: All given inputs are in lowercase letters a-z.

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
# My Answer:---------------------------------------------
        if not strs:
            return ""                               # .....以 ["flower","flow","flight"] 為例............
        short_str = min(strs, key = len)            # short_str = flow 找出最短字串
        for letters in strs:                        # 1) j = 0, flight[0] = flow[0], True
            for j in range(len(short_str)):         # 2) j = 1, flight[1] = flow[1], True
                if letters[j] == short_str[j]:      # 3) j = 2, flight[0] 不等於 flow[2], False -> short_str = fl
                    pass
                else:
                    short_str = letters[:j]
                    break
        return short_str
# Simple Solution--------------------------------------------------------
        if not strs:
            return ""
        for i, letter_group in enumerate(zip(*strs)):   # strs = ['flower', 'flow', 'flight']
        # zip(*strs) => [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
            if len(set(letter_group)) > 1:  # ('f'), ('l'), ('o', 'i'), ('w', 'g')
                # print(i,'return:',strs[0][:i])
                return strs[0][:i]

        else:
            return min(strs)


if __name__ == '__main__':
    strs = list(input().split())
    lcp = Solution()
    print(lcp.longestCommonPrefix(strs))
# 13 Roman to Integer   (Easy)  ✓
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1               4 is Not IIII   ->  IV
# V             5               9 is Not VIIII  ->  IX
# X             10              There are six instances where subtraction is used:
# L             50              I can be placed before V (5) and X (10) to make 4 and 9. 
# C             100             X can be placed before L (50) and C (100) to make 40 and 90.
# D             500             C can be placed before D (500) and M (1000) to make 400 and 900.
# M             1000

''' 2 -> II      12 -> XII     27 -> XXVII
Roman numerals are usually written largest to smallest from left to right.
'''
# Given a roman numeral, convert it to an integer. 
# Input is guaranteed to be within the range from 1 to 3999.
'''                                                                                     << 羅馬數字 轉成 阿拉伯數字 >>
Input: "III"        Input: "IV"         Input: "IX"         Input: "LVIII"  
Output: 3           Output: 4           Output: 9           Output: 58

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.'''

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        Roman_dict_new = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        sum_list = []
        for rom in Roman_dict_new:                          # ......... 以 MCMXCIV 為例 .......................    
            if rom in s:                                    # IV 在 MCMXCIV 中 -> s = MCMXC, sum_list = [4]
                s = s.replace(rom,'')                       # XC 在 MCMXC 中 -> s = MCM, sum_list = [4, 90]
                sum_list.append(Roman_dict_new[rom])        # CM 在 MCM 中 -> s = M, sum_list = [4, 90, 900]
        for r in s:                                         # M 在 M 中 -> s =  , sum_list = [4, 90, 900, 1000]
            sum_list.append(Roman_dict[r])                  # Ans = 4 + 90 + 900 + 1000 = 1994
        return sum(sum_list)                                # ..................................................

if __name__ == '__main__':
    s = str(input())
    sol = Solution()
    print(sol.romanToInt(s))
                


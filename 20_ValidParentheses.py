# 20 Valid Parentheses 有效 括弧 (Easy)  ✓
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.   同類型
# 2. Open brackets must be closed in the correct order.           順序 : 左括號,右括號
# Note that an empty string is also considered valid.
'''                                                                                         << 檢測是否為有效括號 >>
Input: "()"         Input: "()[]{}"     Input: "([)]"       Input: "{[]}"           
Output: true        Output: true        Output: false       Output: true
'''

class Solution:
    def isValid(self, s):
# Simple Solution--------------------------------------------------------        
        stack = []                                              # ........... 以 {[]} 為例 .................   
        dictP = {"]":"[", "}":"{", ")":"("}                     # values: { 在 {[]} 中,(增加) stack = ['{']
        for char in s:                                          # values: [ 在 {[]} 中,(增加) stack = ['{', '[']          
            if char in dictP.values():                          #  keys:  ] 在 {[]} 中,(移除最後一項) stack = ['{']         
                stack.append(char)                              #  keys:  } 在 {[]} 中,(移除最後一項) stack = []     
            elif char in dictP.keys():                          # .........................................  
                if stack == [] or dictP[char] != stack.pop():   # === dict.keys() / dictP.values() / list.pop() =============================                                          
                    return False                                # dict = {k1:v1, k2:v2, ...    => dict.keys() = dict_values([k1, k2,..., kn])
            else:                                               #                 ...,kn:vn}   => dict.values() = dict_keys([v1, v2,..., vn])            
                return False                                    # pop 拋出，表示移除 ; pop() : 移除最後一項     
                                                                # ===========================================================================
        return stack == []      # if return stack == []: return True 
                                # else: return False


if __name__ == '__main__':
    s = str(input())
    sol = Solution()
    print(sol.isValid(s))
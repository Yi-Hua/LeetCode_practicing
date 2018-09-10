# 771. Jewels and Stones
# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  
# Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
# The letters in J are guaranteed distinct, and all characters in J and S are letters. 
# Letters are case sensitive, so "a" is considered a different type of stone from "A".
''' Example :
Input: J = "aA", S = "aAAbbbb"      Input: J = "z", S = "ZZ"
Output: 3                           Output: 0                   '''

# Note:
# S and J will consist of letters and have length at most 50.
# The characters in J are distinct.

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        j = set(list(J))
        s = list(S)
        for i in s:
            if i in j:
                count += 1
        return count


if __name__ == '__main__':
    J = input()
    S = input()
    sol = Solution()
    print(sol.numJewelsInStones(J,S))
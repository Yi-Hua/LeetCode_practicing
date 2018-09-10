# 461. Hamming Distance 漢明距離  (Easy)  ✓
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, calculate the Hamming distance.
# Note: 0 ≤ x, y < 231. 
''' Example: 
Input: x = 1, y = 4         1   (0 0 0 1)             << 漢明距離: 不一樣位置之數量 >> 
Output: 2                   2   (0 0 1 0)             << 找出x,y二進位的漢明距離 >>
                            3   (0 0 1 1)
Explanation:                4   (0 1 0 0)
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different. '''

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
# My Answer---------------------------------------------------------------------------
        # H = []
        # for i in sorted([x,y]):
        #     B = []
        #     while i//2 != 0:    
        #         B.append(i%2)
        #         i = i//2
        #     B.append(i)
        #     H.append(B)                       # bin(x), bin(y) 
       
        # a, b = H[1], H[0]
        # while len(a) > len(b):
        #     b.append(0)  
        # a.reverse()                           # reverse(): 倒序
        # b.reverse()
        # n = 0
        # for i in range(len(a)):               # 找出有不相同的位置    
        #     if a[i] != b[i]:
        #         n += 1
        # return n
# One Line Solution ---------------------------------------------------------------------       
        # return bin(x^y).count('1')
# Solution ------------------------------------------------------------------------------
        count = 0
        while(x or y):
            if x%2 != y%2:
                count += 1
            x //=2              # x //=2 即 x = x // 2
            y //=2              # y //=2 即 x = y // 2
        return count


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    sol = Solution()
    print(sol.hammingDistance(x,y))

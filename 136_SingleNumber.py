# 136. Single Number  (Easy)  ✓
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
''' Example :
Input: [2,2,1]          Input: [4,1,2,1,2]      << 找出list中唯一不重複的數 >>
Output: 1               Output: 4           '''


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # -----------------------------------------
        # for i in nums:                    # Status: Time Limit Exceeded
        #     if(nums.count(i)==1):
        #         return i
        # -----------------------------------------
        return sum(list(set(nums)))*2 - sum(nums)

if __name__ == '__main__':
    s = list(map(int,input().split()))
    sol = Solution()
    print(sol.singleNumber(s))





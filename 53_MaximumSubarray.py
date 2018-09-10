# 53. Maximum Subarray 找連續子集的最大總和 (Easy)  ✓
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
''' Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],             << 給定整數數組nums，找到具有最大總和的連續子集，並回傳其總和>>
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''
# Follow up:
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
# Excellent Solution in Discuss ---------------------------------------------------------------------
        for i in range(1, len(nums)):       # ....................以 [-2, 1,-3, 4,-1, 2, 1,-5, 4] 為例......
            if nums[i-1] > 0:               # -2 < 0, False          [-2, 1...
                nums[i] += nums[i-1]        # 1 > 0, True, -3 -> -2, [-2, 1,-2...
        return max(nums)                    # -2 < 0, False          [-2, 1,-2, 4...
                                            # 4 > 0, True, -1 ->  3, [-2, 1,-2, 4, 3...    
                                            # 3 > 0, True,  2 ->  5, [-2, 1,-2, 4, 3, 5...   
                                            # 5 > 0, True,  1 ->  6, [-2, 1,-2, 4, 3, 5, 6...   
                                            # 6 > 0, True, -5 ->  1, [-2, 1,-2, 4, 3, 5, 6, 1...   
                                            # 1 > 0, True,  4 ->  5, [-2, 1,-2, 4, 3, 5, 6, 1, 5]   
                                            # .........................................................

if __name__ == '__main__':
    s = list(map(int,input().split()))
    sol = Solution()
    print(sol.maxSubArray(s))




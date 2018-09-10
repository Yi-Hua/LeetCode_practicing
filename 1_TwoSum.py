# 1_Two Sum (Easy)  ✓
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''Example:                                                      
Given nums = [2, 7, 11, 15], target = 9,                << 找出數列中，相加為9的兩數的位置 >>
                                                               
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].                                     '''
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
class Solution:
    def twoSum(self, nums, target): #Find two nums whose sum = target.
        """ :type nums: List[int]
            :type target: int
            :rtype: List[int] """
        if len(nums) <= 1:      # If number of nums last than two, we can't get the sum. 
            return False
        sum_dict = {}           # dict              # .......逐一找出互補數，放入dict中>.......
        for i in range(len(nums)):                  # 1) i = 0, False -> sum_dict = {7:0} 
            if nums[i] in sum_dict:                 # 2) i = 1, True  -> return [0,1] 
                return [sum_dict[nums[i]], i]       # End -> 跳出迴圈
            else:                                   # .......................................
                sum_dict[target - nums[i]] = i      # a+b = target
                # print(sum_dict)                   # b = nums[i] => a = target - nums[i}
        # --------------------------------------------------------------------
                                                        

if __name__ == '__main__':
    input_nums = list(map(int,input().split()))
    input_target = int(input())
    sol = Solution()
    a = sol.twoSum(input_nums, input_target)
    print(a)






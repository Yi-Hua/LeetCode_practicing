# 27. Remove Element 刪除元素  (Easy)  ✓
# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
''' Example 1:
Given nums = [3,2,2,3], val = 3,                                                        << 刪除所有指定的元素 >>
刪除所有3
Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.    '''

''' Example 2:
Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.   '''

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """                             # ==== try: === except: ====        # .....以 [3, 2, 2, 3], val = 3 為例.....
        try:                            # try:                              # [3, 2, 2, 3] -> [2, 2, 3] -> [2, 2]
            while True:                 #       嘗試可能發生的               # 逐一刪掉 3 ，用 try; except  
                nums.remove(val)        # except:                           # ......................................    
        except:                         #       例外的情況    
            return len(nums), nums      # ==========================

if __name__ == '__main__':
    s = list(map(int,input().split()))
    v = int(input())
    sol = Solution()
    n, nums = sol.removeElement(s,v)
    print(nums)
     

# Clarification:
# Confused why the returned value is an integer but your answer is an array?
# Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.
# Internally you can think of this:
# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeElement(nums, val);

# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len elements.
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
#}
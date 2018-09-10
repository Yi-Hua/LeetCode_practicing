# 35. Search Insert Position 搜索插入位置   (Easy)  ✓
# Given a sorted array and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.

''' Example                                                                                      << 搜索應插入之位置 >> 
Input: [1,3,5,6], 5     Input: [1,3,5,6], 2     Input: [1,3,5,6], 7     Input: [1,3,5,6], 0
Output: 2               Output: 1               Output: 4               Output: 0               
'''

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """                                         
        nums.append(target)                 # ===== set():刪除重複元素 => type: set ======== 
        list_ = sorted(set(nums))          # ===== sored():按照順序 => type: list =========  
        return list_.index(target)          # ===== list.index(x): 找出 x 的位置 ===========
                                            # ===== list.append(x): 在 list 最末加上 x ===== 


if __name__ == '__main__':
    s = list(map(int,input().split()))
    n = int(input())
    sol = Solution()
    print(sol.searchInsert(s,n)) 





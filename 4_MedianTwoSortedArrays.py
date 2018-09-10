# 4. Median of Two Sorted Arrays   (Hard)  ✓
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.
''' Example 1:
nums1 = [1, 3]                  nums1 = [1, 2]
nums2 = [2]                     nums2 = [3, 4]

The median is 2.0               The median is (2 + 3)/2 = 2.5   '''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)
        l = len(nums)
        if l % 2 == 0:
            return (nums[l//2-1] + nums[l//2])/2
        else:
            return nums[(l-1)//2]

if __name__ == '__main__':
    l1 = list(map(int,input().split()))
    l2 = list(map(int,input().split()))
    sol = Solution()
    print(sol.findMedianSortedArrays(l1,l2))





# =============================================================================
#   FileName: 4.FindMedianSortedArrays.py
#    Example:
#      Input: nums1 = [1, 3]; nums2 = [2]
#     Output: The median is 2.0
#     Author: Marslo
#      Email: marslo.jiao@gmail.com
#    Created: 2016-06-21 18:03:20
#    Version: 0.0.1
# LastChange: 2016-07-05 18:27:35
# =============================================================================


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # temp = []
        for i, j in zip(nums1, nums2):
            print i, '->', j

n11 = [1, 3, 5, 7]
n12 = [2, 4, 6]
r1 = 4

s = Solution()

print '='*100
print ['1 succeed' if r1 == s.findMedianSortedArrays(n11, n12) else '1 failed']

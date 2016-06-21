# =============================================================================
#   FileName: 1.TwoSum.py
#    Example:
#       Given nums = [2, 7, 11, 15], target = 9,
#       Because nums[0] + nums[1] = 2 + 7 = 9,
#       return [0, 1].
#     Author: Marslo
#      Email: marslo.jiao@gmail.com
#    Created: 2016-06-21 15:03:20
#    Version: 0.0.1
# LastChange: 2016-06-21 15:03:20
# =============================================================================


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for ind, item in enumerate(nums):
            x = target - item
            if x in nums[ind+1::]:
                return [ind, nums[ind+1::].index(x)+ind+1]
            elif ind == len(nums)-1 and 0 not in nums:
                return [nums.index(target)]


n1 = [-3, 4, 3, 90]
t1 = 0
l1 = [0, 2]

n2 = [6, 1, 3]
t2 = 6
l2 = [0]

n3 = [0, 1, 2, 0]
t3 = 0
l3 = [0, 3]

n4 = [1, 2, 5]
t4 = 3
l4 = [0, 1]

n5 = [3, 2, 4]
t5 = 6
l5 = [1, 2]

n6 = [572, 815, 387, 418, 434, 530, 376, 190, 196, 74, 830, 561, 973, 771, 640, 37, 539, 369, 327, 51, 623, 575, 988, 44, 659, 48, 22, 776, 487, 873, 486, 169, 499, 82, 128, 31, 386, 691, 553, 848, 968, 874, 692, 404, 463, 285, 745, 631, 304, 271, 40, 921, 733, 56, 883, 517, 99, 580, 55, 81, 232, 971, 561, 683, 806, 994, 823, 219, 315, 564, 997, 976, 158, 208, 851, 206, 101, 989, 542, 985, 940, 116, 153, 47, 806, 944, 337, 903, 712, 138, 236, 777, 630, 912, 22, 140, 525, 270, 997, 763, 812, 597, 806, 423, 869, 926, 344, 494, 858, 519, 389, 627, 517, 964, 74, 432, 730, 843, 673, 985, 819, 397, 607, 34, 948, 648, 43, 212, 950, 235, 995, 76, 439, 614, 203, 313, 180, 760, 210, 813, 920, 229, 615, 730, 359, 863, 678, 43, 293, 978, 305, 106, 797, 769, 3, 700, 945, 135, 430, 965, 762, 479, 152, 121, 935, 809, 101, 271, 428, 608, 8, 983, 758, 662, 755, 190, 632, 792, 789, 174, 869, 622, 885, 626, 310, 128, 233, 82, 223, 339, 771, 741, 227, 131, 85, 51, 361, 343, 641, 568, 922, 145, 256, 177, 329, 959, 991, 293, 850, 858, 76, 291, 134, 254, 956, 971, 718, 391, 336, 899, 206, 642, 254, 851, 274, 239, 538, 418, 21, 232, 706, 275, 615, 568, 714, 234, 567, 994, 368, 54, 744, 498, 380, 594, 415, 286, 260, 582, 522, 795, 261, 437, 292, 887, 405, 293, 946, 678, 686, 682, 501, 238, 245, 380, 218, 591, 722, 519, 770, 359, 340, 215, 151, 368, 356, 795, 91, 250, 413, 970, 37, 941, 356, 648, 594, 513, 484, 364, 484, 909, 292, 501, 59, 982, 686, 827, 461, 60, 557, 178, 952, 218, 634, 785, 251, 290, 156, 300, 711, 322, 570, 820, 191, 755, 429, 950, 18, 917, 905, 905, 126, 790, 638, 94, 857, 235, 889, 611, 605, 203, 859, 749, 874, 530, 727, 764, 197, 537, 951, 919, 24, 341, 334, 505, 796, 619, 492, 295, 380, 128, 533, 600, 160, 51, 249, 5, 837, 905, 747, 505, 82, 158, 687, 507, 339, 575, 206, 28, 29, 91, 459, 118, 284, 995, 544, 3, 154, 89, 840, 364, 682, 700, 143, 173, 216, 290, 733, 525, 399, 574, 693, 500, 189, 590, 529, 972, 378, 299, 461, 866, 326, 43, 711, 460, 426, 947, 391, 536, 26, 579, 304, 852, 158, 621, 683, 901, 237, 22, 225, 59, 52, 798, 262, 754, 649, 504, 861, 472, 480, 570, 347, 891, 956, 347, 31, 784, 581, 668, 127, 628, 962, 698, 191, 313, 714, 893]
t6 = 101
l6 = [83, 239]

n7 = [6, 2, 4]
t7 = 6
l7 = [1, 2]

n8 = [2, 1, 9, 4, 4, 56, 90, 3]
t8 = 8
l8 = [3, 4]


s = Solution()

if l1 != s.twoSum(n1, t1):
    print '1 failed'
else:
    print '1 succeed'

if l2 != s.twoSum(n2, t2):
    print '2 failed'
else:
    print '2 succeed'

if l3 != s.twoSum(n3, t3):
    print '3 failed'
else:
    print '3 succeed'

if l4 != s.twoSum(n4, t4):
    print '4 failed'
else:
    print '4 succeed'

if l5 != s.twoSum(n5, t5):
    print '5 failed'
else:
    print '5 succeed'

if l6 != s.twoSum(n6, t6):
    print '6 failed'
else:
    print '6 succeed'

if l7 != s.twoSum(n7, t7):
    print '7 failed'
else:
    print '7 succeed'

if l8 != s.twoSum(n8, t8):
    print '8 failed'
else:
    print '8 succeed'
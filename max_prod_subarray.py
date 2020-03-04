#Max product subarray
#LC 152

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idea is to get all combinations of values from the given array
        # this can be acheived by multiplying each element in ascending index order
        # and descending index order.
        
        length = len(nums)
        #for reverse index order, create a duplicate array by reversing nums
        rev_nums = nums[::-1]
        res = []
        if length > 1:
            for i in range(1,length):
                nums[i] *= nums[i-1] or 1
                rev_nums[i] *= rev_nums[i-1] or 1
            res = nums+rev_nums
            return max(res)
        else:
            return nums[0]

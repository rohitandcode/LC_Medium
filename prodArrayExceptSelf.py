""" LC 238. Product of Array Except Self
    https://leetcode.com/problems/product-of-array-except-self/
    Input:  [1,2,3,4]
    Output: [24,12,8,6]
    
    basically, solve without division which would have been easy... multiple all elements and get a result.
    then divide by each element and return thr array..
    but since we cant division, go over the input list twice...
"""
    
    def productExceptSelf(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            ll = [1]*len(nums) #left list
            lr = [1]*len(nums) #right list
            res = [1]*len(nums)
            for i in range(1,len(nums)):  # scanning from left to right
                ll[i] = nums[i-1]*ll[i-1]
            for j in range(len(nums)-2, -1, -1): # scanning from right to left
                lr[j] = nums[j+1]*lr[j+1]
            for k in range(len(nums)):
                res[k] = lr[k] * ll[k]
            return res

# LC 398 

import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        arr=[]
        for i in range(len(self.nums)):
            if target == self.nums[i]:
                arr.append(i)
        return random.choice(arr)

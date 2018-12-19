'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

'''
nums = [2, 7, 11, 15]
nums = [2,5,5,11]
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_len = len(nums)
        for i in range(num_len):
            for j in range(i+1, num_len):
                if (nums[i] + nums[j]) == target:
                    return [i, j]

a = Solution()
ret = a.twoSum(nums, 10)
print(ret)


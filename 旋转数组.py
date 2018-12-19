
nums = [1,2,3,4,5,6,7]
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums = [1,2,3,4,5,6,7]
        for i in range(len(nums)):
            if i < k:
                ret = nums.pop()
                nums.insert(0, ret)
        return nums

k = 5
nums = [1,2, 3, 4,5,6,7]
print(nums[-2:])
k=k%len(nums)
print(k)
print(nums[-k:])
print(nums[:-k])
nums[:]=nums[len(nums)-k:]+nums[:len(nums)-k]
print(nums)

# # ****************************
# class Solution:
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         length = len(nums)-1
#         if length <= 1 or k <= 1:
#             pass
#         if length > k:
#             nums.reverse()
#             nums[0:k] = reversed(nums[0:k])
#             nums[k:] = reversed(nums[k:])
#         else:
#             for i in range(k):
#                 nums.insert(0,nums[length])
#                 del nums[length+1]
k = 5
nums = [1,2, 3, 4,5,6,7]
length = k % len(nums)
print(length)
print(nums[-5:])
nums[:] = nums[-length:]+nums[:-length]#倒数-length个参数+从0-（-length）个参数

print(nums)

# 方法
'''
if k > len(nums):
    k = k - len(nums) 
kb = len(nums) - k
tail = nums[-k:]
front = nums[:kb]
nums[:k] = tail
nums[k:] = front

'''
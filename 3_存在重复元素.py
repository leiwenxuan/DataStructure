nums = [1,2,3,4,5,6,7,3,3,43,5,6,6]
nums = [1,2,3,2]
# 数组存在相同的
# print(len(set(nums))== len(nums))

res = 0


# 数组中唯一出现的数
for i in nums:
    res = res ^ i
print(res)
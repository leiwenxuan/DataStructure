nums = [1,3,4,5,6]


#  ----------------------------自己实现48-----------------------
def func(nums):
    nums = list(map(lambda x: str(x), nums))
    int_num = int(''.join(nums))+1
    str_num = [int(i) for i in str(int_num)]
    return str_num
func(nums)


# ---------------------执行44ms实例-----------------------------
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits==[0]:
            return [1]

        l = len(digits)-1
        while l>=0 and digits[l]==9:
            digits[l]=0
            l=l-1
        if digits[0]==0:
            digits.insert(0,1)
        else:
            digits[l]=digits[l]+1
        return digits
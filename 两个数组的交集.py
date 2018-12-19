'''
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。
进阶:

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
'''



nums1 = [1,2,2,1]
nums2 = [2,2]

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ret = []
        for i in nums1:
            if i in nums2:
                nums2.remove(i)
                ret.append(i)
        return ret

        


def func(nums1, nums2):
    dic={}
    ans=[]
    for i in nums2:
        if i in dic:
            dic[i][0]+=1
        else:
            dic[i]=[1,0]
    for i in nums1:
        if i in dic:
            dic[i][1]+=1
    for i in dic:
        if dic[i][1]!=0:
            a=min(dic[i])
            for j in range(a):
                ans.append(i)
    return ans

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        x1 = Counter(nums1)
        x2 = Counter(nums2)
        a = []
        for i in x1.keys():
            if x2[i] != 0:
                num = min(x1[i], x2[i])
                for i2 in range(num):
                    a.append(i)
        return a
        

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1 = {}
        result = []
        for i in nums1:
            dict1[i] = dict1.get(i, 0) + 1
        for i in nums2:
            if dict1.get(i, 0):
                result.append(i)
                dict1[i] -= 1
        
        return result
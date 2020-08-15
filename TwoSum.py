class Solution(object):
    def twoSum(self, nums, target):
        dic = dict((nums[i],i) for i in range(len(nums)))
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dic.keys() and dic[complement] != i:
                return [i, dic[complement]]

nums = list(map(int, input().split()))
target = int(input())
result = Solution()
print(result.twoSum(nums,target))

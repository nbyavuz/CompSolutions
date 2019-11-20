class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resdict = {}
        enumeratednums = enumerate(nums)
        for i, num in enumeratednums:
            if (target - num) in resdict:
                return [resdict[target-num], i]
            resdict[num] = i

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {num:i for i,num in enumerate(nums)}
        for i,num in enumerate(nums):
            ex = hmap.get(target-num,None)
            if ex and not ex==i:
                return i,ex

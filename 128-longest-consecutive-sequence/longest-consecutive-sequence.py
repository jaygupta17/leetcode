class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        mappin = set(nums)
        max_len = 0
        for num in mappin:
            if num-1 not in mappin:
                current = num
                length = 1
                while current+1 in mappin:
                    current += 1
                    length+=1
                max_len = max(length,max_len)
        return max_len 



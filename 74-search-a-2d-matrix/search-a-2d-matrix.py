class Solution:
    def binary(self,nums:List[int],target:int) -> bool:
        start = 0
        end = len(nums)-1
        while start<=end:
            mid = start+(end-start)//2
            if nums[mid]==target:
                return True
            elif target<nums[mid]:
                end = mid-1
            else:
                start=mid+1
        return False
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] == target or row[-1] == target:
                return True
            if row[0] < target and row[-1] > target:
                res = self.binary(row,target)
                return res
        return False

        
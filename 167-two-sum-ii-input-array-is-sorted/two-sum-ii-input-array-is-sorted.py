class Solution:
    def __init__(self):
        for i in range(500):
            self.twoSum([0,0],0)


    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right = 0,len(numbers)-1
        while left<right:
            curr = numbers[left]+numbers[right]
            if curr == target:
                return left+1,right+1
            if curr > target:
                right-=1
            else:
                left+=1


        
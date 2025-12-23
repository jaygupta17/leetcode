class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        try:
          zero = nums.index(0)
        except:
          zero = None
        for i,num in enumerate(nums):
            if zero and (not i==zero or not num==0):
                answer.append(0)
                continue
            if i == 0 or num==0:
              nums[i] = 1
              answer.append(
                  reduce(lambda x,y: x*y,nums)
              )
              nums[i] = num
              continue
            answer.append((answer[-1]*nums[i-1])//num)
        return answer
            
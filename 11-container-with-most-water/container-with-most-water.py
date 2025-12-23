class Solution:
    def maxArea(self, height: List[int]) -> int:
        start,end = 0, len(height)-1
        prev = 0
        while start <=end:
            if height[start] <= height[end]:
                if prev < ((end-start)*(height[start])):
                    prev = ((end-start)*(height[start]))
                start += 1
                continue
            if height[start] > height[end]:
                if prev < ((end-start)*(height[end])):
                    prev = ((end-start)*(height[end]))
                end -= 1
                continue
        return prev



        
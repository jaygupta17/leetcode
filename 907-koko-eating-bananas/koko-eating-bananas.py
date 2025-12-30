class Solution:

    def search(self,start:int,end:int,h:int,piles) -> int:
        while start<end:
            # print(f"start,end = {start},{end}")
            mid = start+(end-start)//2
            # print(f"Mai yaha hu: {mid}")
            hrs = self.get_hours(piles,mid)
            # print(f"hrs needed here: {hrs}")
            if hrs <= h :
                # print(f"hrs<h")
                end = mid
                # print(f"new_end: {end}")
            elif hrs > h:
                # print(f"hrs>h")
                start = mid+1
                # print(f"new_start: {start}")
        return end

    def get_hours(self,piles:List[int],k:int) -> int:
        hrs = sum([math.ceil(num/k) for num in piles])
        return hrs

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = 1
        max_speed = max(piles)

        return self.search(min_speed,max_speed,h,piles)
        



        
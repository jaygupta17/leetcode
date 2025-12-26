class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_num = sorted(nums)
        k = 1
        pairs = set()
        for num in sorted_num:
            start = k
            end = len(sorted_num)-1
            while start<end:
                if sorted_num[start] + sorted_num[end] == -num:
                    pairs.add((
                        sorted_num[start],sorted_num[end],num
                    ))
                    start +=1
                    end-=1
                elif sorted_num[start] + sorted_num[end] > -num:
                    end-=1
                else:
                    start+=1
            k+=1
        return [list(pair) for pair in pairs]


        # nums_set = set(nums)
        # if len(nums_set)==1:
        #     return [] if not nums[0]==0 else [nums[:3]]
        # nums_sorted = sorted(nums)
        # nums_map = set([(i,num) for i, num in enumerate(nums_sorted)])
        # start = 0
        # end = len(nums)-1
        # pairs = set()
        # while start<end:
        #     num = nums_sorted[start]
        #     num2 = nums_sorted[end]
        #     diff = -(num+num2)
        #     if diff in nums_set:
        #         # el = nums_map[diff]
        #         if (start,diff) in nums_map:
        #             end-=1
        #             continue
        #         if (end,diff) in nums_map:
        #             start+=1
        #             continue
        #         pairs.add(
        #             (num,num2,diff) if num2 < diff else (diff,num,num2) if num > diff else (num,diff,num2)
        #         )
        #         start+=1
        #     else:
        #         start+=1
        
        # return [list(pair) for pair in pairs]

    # --------------------------
        # if len(nums)==3:
        #     return [] if not sum(nums)==0 else [nums]
        # nums = sorted(nums)
        # num_map = {num:i for i,num in enumerate(nums)}
        # start = 0
        # end = len(nums)-1
        # pairs = set()
        # while start<end:
        #     num1,num2 = nums[start],nums[end]
        #     _sum = num1+num2
        #     if 0-_sum not in num_map:
        #         if _sum>=nums[end]:
        #             start+=1
        #         else:
        #             end-=1
        #     else:
        #         el = num_map[0-_sum]
        #         if start==el:
        #             end-=1
        #             continue
        #         if end==el:
        #             start+=1
        #             continue
        #         pairs.add((nums[start],min(nums[end],0-_sum),max(nums[end],0-_sum)))
        #         end-=1
        # return [list(pair) for pair in pairs]



        
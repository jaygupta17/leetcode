class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        bday = 0
        i =0
        while i < len(prices)-1:
            if prices[i+1] < prices[bday]:
                bday+=1
                continue
            else:
                curr = prices[i+1] - prices[bday]
                if profit < curr:
                    profit = curr
                i+=1
        return profit




        
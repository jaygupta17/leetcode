class Solution:
    def bestClosingTime(self, customers: str) -> int:
        freq = Counter(customers)
        min_penalty = (float('inf'),None)
        _y,_n = 0,0
        for i,ch in enumerate(customers):
            if ch == 'Y':
                penalty = (freq.get('Y',0)-_y) * 1 + _n*1
                if min_penalty[0] > penalty:
                    min_penalty = (penalty,i+1)
                _y += 1
            else:
                penalty = (freq.get('Y',0)-_y) * 1 + _n*1
                if min_penalty[0] > penalty:
                    min_penalty = (penalty,i)
                _n += 1
            if min_penalty[0] == penalty:
                    continue
        penalty = (freq.get('Y',0)-_y) * 1 + _n*1
        if min_penalty[0] > penalty:
            min_penalty = (penalty,i+1)
        return min_penalty[1]
        
            


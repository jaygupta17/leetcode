class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]
        i = 2
        while i <= numRows:
            curr = [1]
            j = 1
            while j<i-1:
                curr.append(
                    output[-1][j-1]+output[-1][j]
                )
                j+=1
            curr.append(1)
            output.append(curr)
            i+=1
        return output
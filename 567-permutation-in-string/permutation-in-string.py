class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_counts = Counter(s1)
        i = 0
        j = len(s1)

        while j<=len(s2):
            ch = s2[i]
            if ch not in char_counts:
                i+=1
                j+=1
                continue
            curr_counts = Counter(s2[i:j])
            flag = True
            for char,count in curr_counts.items():
                if not char_counts.get(char,0) == count:
                    flag = False
                    break
            if flag:
                return True
            else:
                i+=1
                j+=1
        return False



        

        
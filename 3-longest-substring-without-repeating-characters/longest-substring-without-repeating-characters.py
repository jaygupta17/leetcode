class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_max = 0
        char_map = {}
        i=0
        while i<len(s):
            if not char_map.get(s[i]):
                char_map[s[i]]=i
            else:
                if curr_max < len(char_map):
                    curr_max=len(char_map)
                i = char_map[s[i]]
                # del char_map[s[i]]
                char_map = {}
            i+=1
        return len(char_map) if len(char_map) > curr_max else curr_max
                


        
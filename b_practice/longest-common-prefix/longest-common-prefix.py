class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # get min length
        min_val = 10000000
        for item in strs:
            min_val = min(min_val, len(item))
        return_str = ''
        
        if len(strs) == 0:
            return ""
        
        for i in range(min_val):
            for item in strs:
                if item[i] != strs[0][i]:
                    return return_str
            return_str += item[i]
            print(return_str)
        
        return return_str
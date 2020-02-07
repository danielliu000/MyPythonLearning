class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if strs == []:
            return ""
        if len(strs) == 1:
            return strs[0]

        split_list = []
        min_str = min(strs, key=len)
        min_len = len(min_str)
        str_list = []


        for i in range(min_len):
            n = 0
            for each in strs:
                if min_str[i] == each[i] and min_str[0] == each[0]:
                    n += 1
            if n == len(strs):
                str_list.append(min_str[i])
            if n == 0:
                return ""

        return ''.join(str_list)

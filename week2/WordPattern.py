class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        pattern_list = [char for char in pattern]
        s_list = str.split()
        # print(pattern_list)
        # print(s_list)
        
        table = dict()
        
        if len(pattern_list) != len(s_list):
            return False
        
        for idx in range(len(pattern_list)):
            #check for double mapped values
            if pattern_list[idx] not in table:
                if s_list[idx] in table.values():
                    return False
                table[pattern_list[idx]] = s_list[idx]
            elif pattern_list[idx] in table and table[pattern_list[idx]] != s_list[idx]:
                return False
        return True
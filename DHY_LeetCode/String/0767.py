
# [767] 重构字符串
#

# @lc code=start
class Solution:
    def reorganizeString(self, S: str) -> str:
        char_map = dict()
        #散列表记录频次
        for each in S:
            if each not in char_map:
                char_map[each] = 1
            else:
                char_map[each] +=1
        #排序
        char_order = sorted(char_map.items(), key= lambda x : x[1], reverse= True)
        #print(char_order)

        output = ""
        if char_order[0][1] > (len(S)+1)/2 :
            return output
        else:
            str_sets = [char_order[0][0] for i in range(char_order[0][1])]
            #print(str_sets) 
            i = 0
            for each in char_order[1:]:
                count = each[1]
                while(count):
                    str_sets[i] += each[0]
                    count -=1
                    if(i+1<len(str_sets)):
                        i += 1
                    else: i=0

            #print(str_sets)
        for each in str_sets:
            output += each
        #print(output)
        return output
# S = "aaabbc"
# sol = Solution()
# sol.reorganizeString(S)

# @lc code=end



# [726] 原子的数量
#

# @lc code=start
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        Atom_map = dict()   #合并重组排序
        Atom_list = []      #分解原子顺序表
        index_stack =[]     #括号记录栈

        length = len(formula)
        i = 0

        #化学式拆分
        while i<length:
            if formula[i] == '(':
                index_stack.append(len(Atom_list))
                #print('(', index_stack[-1], Atom_list)
                i += 1
            if formula[i] == ')':
                #print(')', index_stack[-1], Atom_list)
                num_index=i+1
                while  num_index<length and formula[num_index].isdigit():
                        num_index +=1
                #print(int(formula[j]),'原子下标')
                if num_index<length:
                    num = int(formula[i+1:num_index])
                else:
                    num = int(formula[i+1:])
                for each in Atom_list[index_stack.pop():]:
                    each[1] *= num
                i = num_index
            #原子判别    
            if i<length and formula[i].isupper():
                tmp = formula[i]
                #print('tmp=',tmp)
                j = i+1
                if j<length and formula[j].islower():
                    tmp += formula[j]
                    j = j+1
                    #print('更新tmp=',tmp)
            
                #边界
                if j == length:
                    Atom_list.append([tmp,1])
                    #print('结束 j=',j)
                    i = j
                if j < length:
                    #1. 无下标
                    if  formula[j].isupper() or formula[j]=='(' or formula[j]==')':
                        Atom_list.append([tmp,1])
                        #print('原子无下标, j=',j)
                        i = j
                    #2. 有下标
                    if formula[j].isdigit():
                        num_index = j+1
                        while  num_index<length and formula[num_index].isdigit():
                            num_index +=1
                        #print(int(formula[j]),'原子下标')
                        if num_index<length:
                            Atom_list.append([tmp,int(formula[j:num_index])])
                        else:
                            Atom_list.append([tmp,int(formula[j:])])
                        i = num_index                
                #print('原子有下标',i,Atom_list)
            #print(Atom_list)

        #散列表重组
        for each in Atom_list:
            if each[0] not in Atom_map:
                Atom_map[each[0]] = each[1]
            else:
                Atom_map[each[0]] += each[1]
        output = sorted(Atom_map.keys())
        string = ''
        for each in output:
            num_str = ''
            if Atom_map[each]>1:
                num_str = str(Atom_map[each])
            string  = string + each + num_str
        #print(string)
        return string

# formula = "(NB3)33"
# sol =Solution()
# sol.countOfAtoms(formula)

# @lc code=end

'''
Accepted
28/28 cases passed (48 ms)
Your runtime beats 36.41 % of python3 submissions
Your memory usage beats 100 % of python3 submissions (13.8 MB)
'''
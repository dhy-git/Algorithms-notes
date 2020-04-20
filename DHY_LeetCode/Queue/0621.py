'''
>>>任务调度器
    Category	Difficulty	Likes	Dislikes
    algorithms	Medium (45.41%)	245	-

    给定一个用字符数组表示的 CPU 需要执行的任务列表。
    其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。
    任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。
    CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。
    然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，
    因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。
    你需要计算完成所有任务所需要的最短时间。

    示例 ：
    输入：tasks = ["A","A","A","B","B","B"], n = 2
    输出：8
    解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
        在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，
        而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。 
    
    提示：
    任务的总个数为 [1, 10000]。
    n 的取值范围为 [0, 100]。

'''
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0:
            return len(tasks)
        #建立散列表
        map_task = dict()
        for each in tasks:
            a = ord(each)- ord('A')
            if a not in map_task:
                map_task[a] =1
            else:
                map_task[a] +=1
        x = dict(sorted(map_task.items(),key=lambda item:item[1]))
        print(x)
        large = list(x.popitem())[1]    #最大任务
        space = (large-1)*n
        max_time = space+large
        
        while(x):
            tmp = list(x.popitem())[1]
            if tmp == large:
                if space>0:
                    max_time+=1
                    space -= (large-1)
                else:
                    max_time += tmp
            elif(space>=tmp):
                space -= tmp
            else:
                max_time+= (tmp- space)
                space = 0
        return max_time

'''
tasks = ["A","A","A","B","B","B","B"]
n = 2

sol = Solution()
print(sol.leastInterval(tasks,n))
'''

'''
Accepted
69/69 cases passed (100 ms)
Your runtime beats 79.96 % of python3 submissions
Your memory usage beats 8.33 % of python3 submissions (14 MB)
'''

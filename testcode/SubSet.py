from typing import List
def All_Subset(A: List) -> List:
    n = 2**(len(A))
    for i in range(1,n):
        k = 1
        while k<=len(A):
            if i&(2**(k-1)):
                print(A[k-1],end=' ')
            k+=1
        print('')

test = [1,2,3,4]
All_Subset(test)
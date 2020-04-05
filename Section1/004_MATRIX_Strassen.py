'''
4.2 矩阵乘法的Strassen算法
    根据矩阵乘法定义，n*n矩阵相乘计算程序如下：
    
def Square_Matrix_Multiply(A,B,C):
    for i in range(0,len(A)):
        #print('line',i,':',A[i])
        for j in range(0,len(B[0])):
            C[i][j] = 0
            for k in range(0,len(A[0])):
                C[i][j] += A[i][k]* B[k][j]
    print(C)

A = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
B = [[1,2,3,4],[4,5,6,7],[7,8,9,10]]
C = [[0]*len(A) for row in range(len(B[0]))]
#print(C)
Square_Matrix_Multiply(A,B,C)


'''



# copyright@zhangwenchi at 2019/9/21
import numpy as np
num_addorsub=0
num_mul=0
num_assign=0

def read_matrix(file_path):
    input_matrix = list()
    with open(file_path, 'r') as f:
        txt = f.read()
    for line in txt.split('\n'):
        unput_matrix.extend(line.split())
        matrix = [list() for i in range(0, 6)]
    for i in range(0, 6):
        for j in range(0, 6):
            matrix[i].append(float(input_matrix[i * 6 + j]))
    return matrix

def matrix_add(matrix_a, matrix_b):
    '''
    :param matrix_a:
    :param matrix_b:
    :return:matrix_c=matrix_a+matrix_b
    '''
    rows = len(matrix_a) # get numbers of rows
    columns = len(matrix_a[0]) # get numbers of cols
    matrix_c = [list() for i in range(rows)] # build matrix 2d list
    for i in range(rows):
        for j in range(columns):
            matrix_c_temp = matrix_a[i][j] + matrix_b[i][j]
            global num_addorsub,num_assign
            num_addorsub=num_addorsub+1
            num_assign = num_assign+1
            matrix_c[i].append(matrix_c_temp)
    return matrix_c

def matrix_minus(matrix_a, matrix_b):
    '''
    :param matrix_a:
    :param matrix_b:
    :return:matrix_c=matrix_a-matrix_b
    '''
    rows = len(matrix_a)
    columns = len(matrix_a[0])
    matrix_c = [list() for i in range(rows)]
    for i in range(rows):
        for j in range(columns):
            matrix_c_temp = matrix_a[i][j] - matrix_b[i][j]
            global num_addorsub,num_assign
            num_addorsub = num_addorsub + 1
            num_assign=num_assign+1
            matrix_c[i].append(matrix_c_temp)
    return matrix_c

def matrix_divide(matrix_a, row, column):
    '''
    :param matrix_a:
    :param row:
    :param column:
    :return: matrix_b=matrix_a(row,column) to divide matrix_a
    '''
    length = len(matrix_a)
    matrix_b = [list() for i in range(length // 2)]
    k = 0
    for i in range((row - 1) * length // 2, row * length // 2):
        for j in range((column - 1) * length // 2, column * length // 2):
            matrix_c_temp = matrix_a[i][j]
            matrix_b[k].append(matrix_c_temp)
            k += 1
    return matrix_b

def matrix_merge(matrix_11, matrix_12, matrix_21, matrix_22):
    '''
    :param matrix_11:
    :param matrix_12:
    :param matrix_21:
    :param matrix_22:
    :return:mariix merged by 4 parts above
    '''
    length = len(matrix_11)
    matrix_all = [list() for i in range(length * 2)]  # build a matrix of double rows
    for i in range(length):
        # for each row. matrix_all list contain row of matrix_11 and matrix_12
        matrix_all[i] = matrix_11[i] + matrix_12[i]
    for j in range(length):
        # for each row. matrix_all list contain row of matrix_21 and matrix_22
        matrix_all[length + j] = matrix_21[j] + matrix_22[j]
    return matrix_all

def strassen(matrix_a, matrix_b):
    '''
    :param matrix_a:
    :param matrix_b:
    :return:matrix_a * matrix_b
    '''
    rows = len(matrix_a)
    if rows == 1:
        matrix_all = [list() for i in range(rows)]
        matrix_all[0].append(matrix_a[0][0] * matrix_b[0][0])
    elif(rows % 2 ==1):
        matrix_a_np = np.array(matrix_a)
        matrix_b_np = np.array(matrix_b)
        matrix_all = np.dot(matrix_a_np,matrix_b_np)
        global num_mul,num_addorsub
        num_mul = num_mul + 27
        num_addorsub=num_addorsub + 18
    else:
        # 10 first parts of computing
        s1 = matrix_minus((matrix_divide(matrix_b, 1, 2)), (matrix_divide(matrix_b, 2, 2)))
        s2 = matrix_add((matrix_divide(matrix_a, 1, 1)), (matrix_divide(matrix_a, 1, 2)))
        s3 = matrix_add((matrix_divide(matrix_a, 2, 1)), (matrix_divide(matrix_a, 2, 2)))
        s4 = matrix_minus((matrix_divide(matrix_b, 2, 1)), (matrix_divide(matrix_b, 1, 1)))
        s5 = matrix_add((matrix_divide(matrix_a, 1, 1)), (matrix_divide(matrix_a, 2, 2)))
        s6 = matrix_add((matrix_divide(matrix_b, 1, 1)), (matrix_divide(matrix_b, 2, 2)))
        s7 = matrix_minus((matrix_divide(matrix_a, 1, 2)), (matrix_divide(matrix_a, 2, 2)))
        s8 = matrix_add((matrix_divide(matrix_b, 2, 1)), (matrix_divide(matrix_b, 2, 2)))
        s9 = matrix_minus((matrix_divide(matrix_a, 1, 1)), (matrix_divide(matrix_a, 2, 1)))
        s10 = matrix_add((matrix_divide(matrix_b, 1, 1)), (matrix_divide(matrix_b, 1, 2)))
        # 7 second parts of computing
        p1 = strassen(matrix_divide(matrix_a, 1, 1), s1)
        p2 = strassen(s2, matrix_divide(matrix_b, 2, 2))
        p3 = strassen(s3, matrix_divide(matrix_b, 1, 1))
        p4 = strassen(matrix_divide(matrix_a, 2, 2), s4)
        p5 = strassen(s5, s6)
        p6 = strassen(s7, s8)
        p7 = strassen(s9, s10)
        # 4 final parts of result
        c11 = matrix_add(matrix_add(p5, p4), matrix_minus(p6, p2))
        c12 = matrix_add(p1, p2)
        c21 = matrix_add(p3, p4)
        c22 = matrix_minus(matrix_add(p5, p1), matrix_add(p3, p7))
        matrix_all = matrix_merge(c11, c12, c21, c22)
        global num_assign
        num_assign =num_assign+22
    return matrix_all

def main():
    # read data
    A = read_matrix('matrixA.txt')
    B = read_matrix('matrixB.txt')
    # compute A*B
    C = strassen(A,B)
    print("\nResult of matrix given\n",np.array(C))

    # verificate A*B
    C_verification=np.dot(A,B)
    print("\nSubtract from standard results\n",np.array((C-C_verification),dtype=int))
    # statistical data
    print("\nfrequency of add/sub",num_addorsub)
    print("frequency of assign", num_assign)
    print("frequency of mul", num_mul)
    new_matrixA = np.random.random_integers(-5,5,size=(8, 8))
    print("\nRandom Matrix A:\n", new_matrixA)
    new_matrixB = np.random.random_integers(-5,5,size=(8, 8))
    print("\nRandom Matrix B:\n", new_matrixB)

    AdotB=strassen(new_matrixA, new_matrixB)
    print("\n A*B Result of matrixs by generate randomly\n",np.array(AdotB))

    BdotA = strassen(new_matrixB, new_matrixA)
    print("\n B*A Result of matrixs by generate randomly\n", np.array(BdotA))

    result=new_matrixA
    for i in range(0,2019):
        result=strassen(result,new_matrixA)
        print("\n A^2019 Result of matrixs by generate randomly\n",np.array(result))


if __name__ == '__main__':
    main()
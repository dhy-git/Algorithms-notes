def Bubble_Sort(array):
    for i in range(1, len(array)):
        j = 0
        while(j< (len(array)-i) and array[j]> array[j+1]):
            #swap:
            array[j],array[j+1] = array[j+1],array[j]
            j += 1
    print(array)
#test:
a = [7,6,5,4,3,2,1]
Bubble_Sort(a)
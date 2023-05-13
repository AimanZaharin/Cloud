#Insertion Sort
 
array = [5, 9, 3, 1, 2, 8, 4, 7, 6] 

n = len(array)

for i in range(1, n):
     
    stopper = array[i]

    j = i - 1

    while j >=0 and stopper < array[j]:
        array[j+1] = array[j]
        j -= 1
    array[j+1] = stopper

for i in range(len(array)):
    print("%d" %array[i],end=" ")
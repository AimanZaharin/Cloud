#bubble Sort

array = [5, 9, 3, 1, 2, 8, 4, 7, 6]

n = len(array)

for i in range(n):

    for j in range(0, n-i-1):
        
        #Swapping process
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]

for i in range(len(array)):
    print("%d" %array[i],end=" ")

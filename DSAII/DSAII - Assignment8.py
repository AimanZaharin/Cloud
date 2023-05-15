#Selection Sort

import sys
Array = [5, 9, 3, 1, 2, 8, 4, 7, 6]
 
# Prcoess through all elements inside the array
for i in range(len(Array)):
     
    # Find the minimum element in the array
    minimum = i

    for j in range(i+1, len(Array)):
        if Array[minimum] > Array[j]:
            minimum = j
             
    # Swapping process     
    Array[i], Array[minimum] = Array[minimum], Array[i]

for i in range(len(Array)):
    print("%d" %Array[i],end=" ")
# Q3) Modify your code in no.1 to 
# write a code for Fibonacci 
# (recursive DP) - make a branch

def fibonacci(n):
     
    temp = [0, 1]
     
    for i in range(2, n+1): #2 TO 6
        temp.append(fibonacci(n-1) + fibonacci(n-2))
    
    return temp[n]

def main():
    
    n = 6

    print(fibonacci(n))

main()

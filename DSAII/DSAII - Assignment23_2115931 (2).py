# Q2) Modify your code in no.1 to write a 
# code for Fibonacci (iterative DP) - make a branch

def fibonacci(n):

    temp = [0, 1]

    for i in range(2, n+1):
        temp.append(temp[i-1] + temp[i-2])

    return temp[n]

def main():
    
    n = 6

    print(fibonacci(n))

main()
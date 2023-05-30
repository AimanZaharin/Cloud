# Q1) Write a code for finding nth Fibonacci number 
# (recursion without dynamic programming (DP))

def fibonacci(n):

    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

def main():
    
    n = 6

    print(fibonacci(n))

main()

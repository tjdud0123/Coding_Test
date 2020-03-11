def solution(n):
    fibo0, fibo1, fibo2 = 0, 1, 1
    
    for _ in range(n):
        fibo2 = fibo1 + fibo0
        fibo0 = fibo1
        fibo1 = fibo2
        
    return fibo2 % 1000000007
def sieve(n):
    primes = [True] *(n+1)
    for i in range(2,int(n** 0.5)+1):
        if primes[i]:
            for j in range(i**2,n+1,i):
                primes[j]=False
    for i in range(2,n+1):
        if primes[i]:
            print(i,end = ' ')
n=int(input("Enter the value of n:"))
sieve(n) #O(n log log n)
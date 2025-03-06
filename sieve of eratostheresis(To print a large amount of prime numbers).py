def sieve(n):
    res=[]
    primes = [True] *(n+1)
    for i in range(2,int(n** 0.5)+1):
        if primes[i]:
            for j in range(i**2,n+1,i):
                primes[j]=False
    for i in range(2,n+1):
        if primes[i]:
            res.append(i)
    return res
def segmentedSieve(n):
    primes=[]
    limit=int(n**0.5)+1
    primes=sieve(limit)
    for low in range(limit+1,n+1,limit):
        high=min(low+limit-1,n)
        segment =[True]*(high-low+1)
        for p in primes:
            if p*p > high:
                break
            firstMultiple = (low)//p*p
            if firstMultiple < low:
                firstMultiple += p
            for i in range(firstMultiple , high+1,p):
                segment[i-low]= False
        for i in range(low,high+1):
            if segment[i-low]:
                primes.append(i)
    return primes
n=int(input("Enter the value of n: "))
res = segmentedSieve(n)
print(res)

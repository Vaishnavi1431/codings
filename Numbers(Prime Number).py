def isPrime(n):
    if n <= 1:
       return False

    for i in range(2, int(n**0.5) + 1):
       if n % i == 0:
         return False

    return True
n=int(input("Enter a number:"))
if(isPrime(n)):
   print(n,"is a prime number")
else:
   print(n,"is not a prime number")
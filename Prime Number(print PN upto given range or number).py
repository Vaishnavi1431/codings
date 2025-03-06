def isPrime(n):
  for elt in range(2, n**0.5):
    if (n % elt == 0):
      return False
  return True

def primesUptoN(n):
    for elt in range(2, n + 1):
        if (isPrime(elt)):
             print(elt)
n=int(input("Enter the number:"))
print(primesUptoN(n))
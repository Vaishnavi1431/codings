def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def print_primes_upto(n):
  for num in range(2, n + 1):
    if is_prime(num):
      print(num, end=" ")
n = int(input("Enter the upper limit: "))
print_primes_upto(n)
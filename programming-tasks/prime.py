def SieveOfEratosthenes(n):
  is_prime = [True]*(n+1);
  is_prime[0] , is_prime[1] = False, False
  for i in range(2, n+1):
      if is_prime[i] and i * i <= n:
          for j in range(i*i, n, i):
              is_prime[j] = False
      
  return ''.join([str(i) for i, elem in enumerate(is_prime) if elem])
primes = SieveOfEratosthenes(15000)
def reid(n):
  
  return primes[n:n+5]

print(reid(10000))


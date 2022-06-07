def factors(n):
  factors=[]
  for i in range(2,n+1):
    if n%i==0:
      factors.append(i)
  return factors

def primeFactors(Factors):
  primes=[]
  for i in Factors:
    prime=factors(i)
    if len(prime)==1:
      primes.append(i)
  return primes
Output=0
n=int(input())
n_factors=factors(n)
n_factors=n_factors[:len(n_factors)-1]
print(n_factors)
for i in range(len(n_factors)//2):
  smallFactor=factors(n_factors[i])
  bigFactor=factors(n_factors[len(n_factors)-i-1])
  if len(smallFactor)>1:
    smallPrimeFactor=primeFactors(smallFactor)
  else:
    smallPrimeFactor=smallFactor
  bigPrimeFactor=primeFactors(bigFactor)
  for j in smallPrimeFactor:
    if j in bigPrimeFactor:
      Output=1
  if Output==1:
    break
print(Output)
  
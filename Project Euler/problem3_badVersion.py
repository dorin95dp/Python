from problem7_better import isPrime
from time import time

def getPrimeFactors(number):
    primeFactors = []
    for i in range(2, number//2 + 1):
        if isPrime(i) and number % i == 0:
            primeFactors.append(i)
            
    return primeFactors

def getLargestPrimeFactor(number):
    primeFactors = getPrimeFactors(number)
    largestPrime = max(primeFactors)
    
    return largestPrime

if __name__ == '__main__':
    initialTime = time()
    number = 200
    largestPrime = getLargestPrimeFactor(number)
    executionTime = time() - initialTime
    print("The largest prime factor of %d = %d"%(number, largestPrime))
    print("Execution time = %r"%(executionTime))

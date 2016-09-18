from problem7_better import isPrime
from time import time

def getPrimeFactors(number):
    primeFactors = []
    if isPrime(number):
        return [1]
    for i in range(2, int(number//2 + 1)):
        if isPrime(i) and number % i == 0:
            primeFactors.append(i)
            dividedPrime = int(number / i)
            primeFactors2 = getPrimeFactors(dividedPrime)
            if primeFactors2 == [1]:
                if primeFactors2 not in primeFactors:
                    primeFactors.append(dividedPrime)
            else:
                for element in primeFactors2:
                    if element not in primeFactors:
                        primeFactors.append(element)
            break
        
            
    return primeFactors

def getLargestPrimeFactor(number):
    primeFactors = getPrimeFactors(number)
    largestPrime = max(primeFactors)
    
    return largestPrime

if __name__ == '__main__':
    initialTime = time()
    number = 600851475143   
    largestPrime = getLargestPrimeFactor(number)
    executionTime = time() - initialTime
    print("The largest prime factor of %d = %d"%(number, largestPrime))
    print("Execution time = %r"%(executionTime))

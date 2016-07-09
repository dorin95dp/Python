"""def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)"""
# too big time complexity of the algorithm O(n^2)

def fib(n):
    const=1
    r=0  # result
    for i in range(1,n):
        r=const+r
        const=r-const
    return r
# time complexity O(n)

n=100 # nr of elements
A = [] # the list
for i in range(1,n+1):
    A.append(fib(i))

print (A)


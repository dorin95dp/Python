A = [1,5,7,10]

def function1(A):
    summ = 0
    for i in range(len(A)):
        summ += A[i]
    return summ
summa = function1(A)
print (summa)

def function2(A):
    i=0
    summ=0
    
    while(i<len(A)):
        summ += A[i]
        i+=1

    return summ
summa2=function2(A)
print(summa2)

def function3(A,i):
    if i == 0:
        return 0
    else:
        return A[i-1] + function3(A,i-1)

i=len(A)
summa3 = function3(A,i)
print (summa3)

"""def Sum(A):
    if len(A)==1:
        return A[0]
    else:
        return A[0]+Sum(A[1:]) 

summa4 = Sum(A)
print(summa4)"""

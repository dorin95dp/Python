#https://www.shiftedup.com/2015/05/08/solution-to-problem-4
def first_digit(n):
    string_n = str(n)
    firstDigit = int(string_n[0])
    return firstDigit
def second_digit(n):
    string_n = str(n)
    secondDigit = int(string_n[1])
    return secondDigit
    

def verif(a,b):
    if first_digit(a)>first_digit(b):
        return a
    elif first_digit(a)==first_digit(b):
        if second_digit(a)>second_digit(b):
            return a
        else:
            return b
    else:
        return b
a=5
b=55
alfa = verif(a,b)
print (alfa)
def Arrange_array(A):
    for passnum in range(len(A)-1,0,-1):
        for i in range(passnum):
            if (verif(A[i],A[i+1])==A[i+1]):
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp
    return A

def Array_to_nr(B):
    temp = ""
    for i in range(len(B)):
        temp += str(B[i])
    N = int(temp)    
    return N

def LargestNr(A):
    B = Arrange_array(A)# B - A array aranged in descending order
                        #                   comparing first digit
    N = Array_to_nr(B)  # N - the largest nr reached from transforming B(array)
    return N

A = [50,2,1,9]
N = LargestNr(A)
print (N)

list1 = [1,2,3]
a= "a,b,c"
list2 = a.split(",")

def funct(a,b):
    list3 = []
    l = len(a)
    
    for i in range(l):
        list3.append(a[i])
        list3.append(b[i])
    return list3

list3 = funct(list2,list1)
print (list3)

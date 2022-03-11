#variable length arg
'''def sum(*n):
    total=0
    for n1 in n:
        total=total+n1
    print("the sum=",total)
sum()
sum(10)
sum(10,20)
sum(10,20,30,40)'''

#variable length arg with keyword arg

'''def f1(*s,n1):
    for s1 in s:
        print(s1)
    print(n1)
f1("A","B",n1=10)'''

#keywordarg
'''def display(**kwargs):
    for k,v in kwargs.items():
        print(k,"=",v)
display(n1=10,n2=20,n3=30)
display(rno=100,name="Durga",marks=70,sub="java")'''

#global var
'''a=10

def f1():
    #a=a+1                #error
    a=15
    print(a)
def f2():
    print(a)
f1()
f2()'''

'''a=10
def f1():
    a=777
    print(a)
    print(globals()['a'])
f1()'''

'''def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
#print("factorial of 4 is:",factorial(4))
#print("factorial of 5 is:",factorial(5))
print(factorial(4))
print(factorial(5))'''

#lambda fun
'''s=lambda n:n*n
print("the sq of 4 is:",s(4))
print("the sq of 5 is:",s(5))'''

'''def isEven(x):
    if x%2==0:
        return True
    else:
        return False
l=[0,5,10,15,20,25,30]
l1=list(filter(isEven,l))
print(l1)
#isEven(l)'''

'''l=[0,5,10,15,20,25,30]
l1=list(filter(lambda x:x%2==0,l))
print(l1)
l2=list(filter(lambda x:x%2!=0,l))
print(l2)
l3=list(map(lambda x:2*x,l))
print(l3)'''

'''l=[1,2,3,4,5]
def doblelt(x):
    return 2*x
l1=list(doublelt)'''

from functools import*
l=[10,20,30,40,50]
result=reduce(lambda x,y:x+y,l)
print(result)
result1=reduce(lambda x,y:x*y,l)
print(result1)









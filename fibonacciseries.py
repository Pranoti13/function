'''def fibonacci(n):
    if n<=1:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
a=eval(input("enter no of terms:"))
if a<=0:
    print("enter +ve no:")
else:
    print("fibonacci series is:")
    for i in range(a):
        print(fibonacci(i))
fibonacci(a)'''

'''def fibonacci(n):
    a=0
    b=1
    c=0

    print(a)
    print(b)
  #  count=2
    
    for i in range(2,n):
        c=a+b
        #count=count+1
        print(c)
        a=b
        b=c
f=eval(input("enter num:"))

fibonacci(f)'''

def fibo(n):
    a=0
    b=1
    c=0
    print(a)
    print(b)
    d=n//2
    for i in range(d,n):
        c=a+b
        print(c)
        a=b
        b=c
a=eval(input("enter num:"))
fibo(a)



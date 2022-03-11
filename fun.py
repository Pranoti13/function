'''def demo():
    a,b=eval(input("accept two no:"))
    print(a,b)
    c=a+b
    print("add=",c)

demo()'''

#passing parameter
'''def demo(p,q):
    c=p+q
    print(c)


a,b=eval(input("accept two no:"))
demo(a,b)'''

#return
'''def demo(p,q):
    c=p+q
    d=p-q
    return c,d
a,b=eval(input("accept two no:"))
sum,diff=demo(a,b)
print(sum)
print(diff)'''

#accept no from user passing to fun print sq cube
'''def demo(n):
    s=n*n
    c=n*n*n
    return s,c
a=eval(input("accept no:"))
sq,cube=demo(a)
print("square=",sq)
print("cube=",cube)'''

'''def demo(n):
    f=1
    for i in range(1,n+1):
        f=f*i

    return f
a=eval(input("accept no:"))
fact=demo(a)
print(fact)'''

#keyword arg
'''def wish(name,msg):
    print("Hello",name,msg)
wish(name="Durga",msg="Good Morning")
wish(msg="Good Morning",name="Durga")'''

#fun with default value
'''def add(a,b,c=0,d=0):
    sum=a+b+c+d
    print(sum)
add(2,3)
add(2,3,4)
add(2,3,4,5)
add(4)    '''               #type error=add()missing 1 required positional arg:'b'

#variable length arg
def add(*n):
    print(n)
    sum=0
    for i in n:
        sum=sum+i
    print(sum)
add(1,2,3,4,5,6,7,8,9,10)

#

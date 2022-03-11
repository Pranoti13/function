def prime(a):
    count=0
    if a>1:
        for i in range(2,a):
            if a%i==0:
                count=count+1
                #print(i)
        if count==2:
            print(a)





n=eval(input("enter no:"))
prime(n)


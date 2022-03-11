#simple programm user defined fun =def fun_name()
'''def wish():
    print("hello Good Morning")
wish()'''

#parameter
#Write a function to take name of the student as input and print wish message by name.
'''def wish(name):
    print("hello",name,"good morning")
    
wish("durga")
wish("ravi")'''

#Write a function to take number as input and print its square value

'''def sq(number):
    print("the sq of",number,"is",number*number)
sq(4)
sq(5)'''

'''def wish(name,msg):
    print("hello",name,msg)
wish(msg="good morning",name="durga")'''

def f1(n1,*s):
    print(n1)
    for s1 in s:
        print(s1)
f1(10,20,30)



#fun=if a group of statemis repetadely required then it is not recommanded to write these statement everytime separately  we have to define these statement as a single unit and we call that unit any no of times based on our requirement without rewriting this unit is nothing but "fun"
'''2type of fun
built fun=id(),type(),input(),eval() etc..
user defined fun=def funname(parameter):
                "doc string"
                 ........
                 ........
                 return value'''

#creating fun we can use 2 keywords=def(mandatory) , return (optional)
#parameter are input to the fun,if a fun contain parameter then at a time of calling compulsory provide value ow we will get error
#return statement:fun can take input values as parameter and execute business logic and return output to the caller with statement

#in python a fun can return any number of values i.e returning multiple value from a fun
#ex 1.
def sum_sub(a,b):
    sum=a+b
    sub=a-b
    return sum,sub
x,y=sum_sub(24,3)
print("sum=",x)
print("sub=",y)

#ex 2.
def calc(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
t=calc(100,50)
print("result are=",t)            #result gives tupple form
for i in t:
    print(i)                  #result gives loop

#type of arg=formal, actual=1)positional 2)keyword 3)default 4)variable length
'''def f1(a,b):                                 #a,b are formal arg
  .........
  ..........

f1(10,20) '''           #10,20 are actual arg

#1)positional arg=1)arg pass to fun in correct positional order
#                 2)no of arg and position of arg must be matched if we change order then result may be changed
#ex1.
def sub(a,b):
    print(a-b)
sub(100,200)
sub(200,100)

#2)keyword arg=we can pass arg value by keyword
#ex1
def wish(name,msg):
    print("hello",name,msg)
wish(name="durga",msg="good morning")
wish(msg="good morning",name="durga")
wish(durga,msg="hello")                    #name error=value of  durga not pass with keyword

#4)variable length arg=we can pass no of arg to our fun such type of arg called variable length arg
#we can declare variable length arg with * symbol

def f1(*n):










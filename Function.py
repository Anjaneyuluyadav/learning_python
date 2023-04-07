# Function : function is a collection of statements in a singggle unit
# we cn call thr functin num of times
# the main adavantagge of functions is code reusability
# function  always starts with def keywoed
# tow types of functions r there
# we can write n num of statements inside the fuction
# funtion calling always should b afteer the fun defination
#1. builtin or predefinned func  -> id ,type,len,pow eval,reversed,sorted
#2) user definced functions -> the functions which r developed by the programmer is called user defined functions
# we can pass n num of arggs in function
# #syntax :
# def function_name(args):
#     #st1
#    #st2
#    #st3

# def hello():
#     print("HELLO FRNDS")
#     print("i m bad")
#     print("ellp")
# hello()

# 1) without args wit return values
# if we are returning some thing from the function means to say must and should wee have to use retuen statememt inside the function
# if u r returning val from fun must and should we have to call the fun
# varname=functionnmae()
# without arggs withh retuen values
# def hello():
#     print("hello frnds")
#     print("HI")
#     return "MY students r good"
# #out=hello()
# hello()
# #print("otput :",hello())
#
# '
# with args without return values
# def add(a,b):
#     print("Addition :",a+b)
#     print("mul",a*b)
#     print("sub",b-a)
# add(10,20)

# wit arggs with return values

# def add(a,b):
#     print("Addition :",a+b)
#     return a*b
# out=add(10,20)
# print('out :',out)
# print("output :",add(10,20))

# without arggs withhout retuen values
# def hello():
#     print("Hi frnds")
#     print("hello python")
# hello()

# # return multiple values from te functions
# def hello(a,b):
#     return a+10,b+10,50,40,100
# x,y,c,d,e=hello(10,20) # 20,30
# print("x val :",x)
# print("y val :",y)
# print("c val",c)
# print("D val ,",d)
# print("e val :",e)

# formal args : the args which we are declared in function def is called formal args
# actual args : the args which we are passing while calling the function is called actual args


#n=int(input("enter n val :"))
# def check_even(num):  # num is formal arg
#     if num%2==0:
#         return num
#     else:
#         return num
# out=check_even(n) # n is actual arg
# print("num is :",out)
#
# for i in range(1,6):
#     print("num is :",check_even(i))

# [1-100] Prime and palindrom num

# the num which is divisible by 1 and with same num is called prime
# the num whih is having only two factors is called prime num
# def Check_Palindrom(n):
#     num=str(n)
# /    if num==num[::-1]:
#         return int(num)
#
#
# def check_prime(n):
#     c=0
#     for i in range(1,n+1):
#         if n%i==0:
#             c=c+1
#     if c==2:
#         return n
#
# Prime_list=[]
# Pal_List=[]
#
# for i in range(1,100):
#     if check_prime(i)!=None:
#         Prime_list.append(i)
#         if Check_Palindrom(i)!=None:
#             Pal_List.append(i)
#
# print("PrimeList:",Prime_list)
# print("Pallist :",Pal_List)
import  math
#print("fact :",math.factorial(5))

# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     return f
#
# for i in range(1,15):
#     print("factorial of {} is {}".format(i,fact(i)))


# positional arggggs : tese args r passed to function in  correct positional order
# nun of arggs must tb same in func defenation and function calling
# def add(a,b):
#     print("add :",a+b)
# add(10,20)

#keyword args : we can pass the args into funtion by usijng keywords
# def add(a,b,c):
#     print("add :",a+b+c)
# add(b=10,a=20,c=30)

#positional + keyword
# if we want to use  both positional +keyword at a time then frst we have to give positional args next we can give keyword args
# def add(a,b,c):
#     print("add :",a+b+c)
# add(100,b=30,c=20)

# default_args : default_args are function paramters  we have to provide the default value
# if we pass the value for the default argument then it will take the value what we passed otherwise it wil take the default vale
# default args always should b the right side of function defination
#
# def add(a,b,c=0,d=0,e=0):
#     print("add :",a+b+c+d+e)
# add(10,20,50,7)

# variable len args :# some times we can pass n no of args to the function  this type of args r called variable len args
# we can declare the varibale len args is *argument name
# variable len argments interally stores the elemnts in the form of tuple
# if we return the variable len argument it will return the tuple
# syntax : def functionnama(*varname)

# def add(*a):
#     print(a)
#     return a
# out=add(1,2,4,5,6,7,8,100,400)
# print(out)

# def sum_ele(*a):
#     s=0
#     for i in a:
#         s=s+i
#     return s
# out=sum_ele(1,2,3,4,5)
# print("out :",out)

#
# def sum_ele(*a):  # [2,4,6]
#
#     # for i in a:
#     #     if i%2==0:
#     #         evenlist.append(i)
#     evenlist=(i for i in a if i%2==0)
#     return list(evenlist)
#
#
# out=sum_ele(1,2,3,4,5,6)
# print("out :",out)



#  positional + variable len

# def hello(a,*b):
#     print(a)
#     print("b val :",b)
#
# hello(100,3,4,5)

# positioinal+variable_len + default
# def hello(a,*b,c=0):
#     print(a)
#     print("b val :",b)
#     print(c)
#
# hello(100,3,4,5,c=700)

# keyword variable len args :
# we can pass n num of args to the functions by specifying keywords in funtion callingg
# these arrgs are stored in te form of dict(keys and val pairs)
#keyword variable len arg will return dict

# syntx def funname(**varname)

# def add(**a):
#     print(a)
#     print(type(a))
# add(x=100,y=200,a='i',b='am',c='gggood')

# variablelen+ keywordvarlen
# def hello(*a,**b):
#     print("a val :",a)
#     print("b val :",b)
#
# hello(1,2,3,5,x='hi',y='hello')


# def hello(**b):
#     print("b val :",b)
#     print(b.items())
#     print(b.keys())
#     print(b.values())
#     print(b.get('x'))
# hello(x='hi',y='hello')

# local variable : te varibale wich is declared inside te funttion is called loacal variable
# scope of te local varibale i s inside te function onlyu
# we cant use the local var outside of hhe function
# def hi():
#     a=100
#     print(" a val :",a)
# hi()
#print(" a val is : ",a)

# def hi(c):
#     a=100
#     print(" a val :",a)
#     print("c val :",c)
# hi(10)

# global variable : te variable whhichh is defind outside of the function is called global varible
# global variable value may chnage in any othher function or any other place outside or inside the function
# if we want to chnage the global varible inside the function we have use keyword callled global
#
# x=100
# def hi():
#     global x
#     print("x val hhi :",x)
#     x=x+200
#     print("global var x :",x)
# hi()
# x=x+20
# def hello():
#     print("x val in hello :",x)
# hello()


# x=200
# def hi():
#     global x
#     print("gglobal var  hi:",x) # 200
#     x=x+30
# def hello():
#     print("hello x :",x)    #  200
# hello()
# hi()
# print("x val :",x) # 230

# use gglobal var and local var wit same name
# local var is always the frst priority
# if we want to use   gglobal var and local var wit same name inside te fun to print global var we have to use notation is globals()[variable name]
#
# x=100
# def hello():
#     x=300
#     print("local x :",x)
#     print("global x :",globals()['x'])
# hello()


# nested functions : function inside the anoter function is called nested functions
# syntax :
# def fun_name1(args):
#     #st21
#     #st2
#     def fun_name2(args) :
#         #st3
#         #st4
#     fun_name2()

# def hi():
#     print("HI studnets")
#     def hello():
#         print("Hello students")
#     hello()
# hi()

# def hi(a,b):
#     print("addition :",a+b)
#     def hello():
#         print("mul :",a*b)
#     hello()
# hi(10,20)

# def hi(a,b):
#     print("addition :",a+b)
#     def hello(c,d):
#         print("names :",c+d)
#         #print("mul :",a*b)
#     hello("rama","krishh")
# hi(10,20)

# function alisinggg : givinggg aliou s name to thhhhe existingg function is called function alisinggg
# syntax : varname=functioname

# def hi():
#     print("Hi students")
# hello=hi
# a=hello
# hello()
# hi()
# a()
# print("address a",id(a))
# print("address of hi",id(hi))
# print("address of hello",id(hello))

# decortor : decortor is a function which takes function as a agrument and it extends the existing functionality
# without touching existing functionality add new feature to the same function
#syntax def fun1(function_name):
             # st1
            #st2
           # return function_name
# @fun1
# def function_name():
#     #st3
#     #st4
# We can like this also we can pass one functioname passing as parameter to the another function
#
# fun1(function_name)
#

# ex :1
# def hi():
#     print("HHI")
#     def hello():
#         print("hello")
#     hello()
# hi()

# def hi(fun_name):
#     print("HI frnds")
#     fun_name()
#
# @hi        # hi(hello)
# def hello():
#     print("hello guys")
# @hi   # hi(student)
# def student():
#     print("my students r good")

#hi(hello)
#hi(student)

# generator: generator is a function wich is responsible for to generate the sequence values
# generator is a normal function only
# generator which is usingg yeild keyword

# the function which is having yeild statement is called generator
# generator generates the sequence of values
# generator internally contains iterator

# def hi():
#     print("HI")
#     print("Helo")
#
# hi()
# hi()
# hi()
# def hi():
#     yield 1
#     yield 2
#     yield 3
#
#
# out=hi()
# print(next(out))
# print(next(out))
# print(next(out))

# to generate n numbers
#def first_num(num):
#     n=1
#     while(n<=num):     #(1,2,3,4,5,6,7,8,9,10)
#         yield n
#         n=n+1
# out=first_num(10)
# print(next(out))  # 1
# print(next(out))  # 2
# print(next(out))  # 3
# print("For loop start :")
# for i in out:
#     print(i,end=' ')

# iter() : iterator is a function it is useful for iterates the elemeents from iterable object
# iterators takes one paramter is called itarable object
# we have to next() -> to featch the next element
# Next() -> it will fetc thhe next ele and olds te previous elemenet position

# syntax : iter(iterable obj)
# x=list(range(1,11)) #[1-10]
#
# out=iter(x)
# print(next(out)) # 1
# print(next(out)) # 2
# for i in out:
#     print(i,end=' ')

# anonmous fun or lambda function : a function wicch is defineed withhout a name is called  anonmous fun or lambda function
# tjhe main purpose of te function is instant use
# we cant write n number of lines usinggg lambda fun
# small codes we write wit lamda functioin

# synatax : var_name= lambda var1,var2 : business logic

# def add(a,b):
#     return a+b
# out=add(10,20)
# print("result :",out)

# kamal =lambda a,b:a+b
#
# print("addition :",kamal(10,20))

# a,b=10,2
# print("power:",pow(a,b))   # pow(10,3) # 10*10*10


# def power(a,b):
#     return pow(a,b)  #(10,2) #10*10
# out=power(10,2)
# print("result :",out)

# bavani =lambda a,b:pow(a,b)
# print("resullt :",bavani(10,2))
#
# def big(a,b):
#     if(a>b):
#         return a
#     else:
#         return b
# print("big :",big(10,20))

# big =lambda a,b : a if(a>b) else b
#
# print("big :",big(20,500))


#filter : it will take two arguments one is fun and iterableobject(list,string,tuple)
# it is useful for to filter the perticuler elements
# syntax :list(filter(function,iterable_obj))

# def even(i):
#     if i%2==0:
#         return i
# for i in range(1,11):
#     if even(i)!=None:
#         print(i,end=' ')

# out=list(filter(even,list(range(1,11))))
# print(out)

# out=list(filter(lambda a:a%2==0,list(range(1,11))))
#
# print("Ele :",out)


# def odd(a):
#   if a%2!=0:
#       return a

#print("result :",odd(3))

#x=list(range(1,11)) #[1,11]
# out=list(filter(odd,x))
# print(out)

# out=list(filter(lambda a:a%2!=0,x))
# print(out)

# map : map will apply on each and every element in iterable object(tuple,list,string)
# it will modify the all the elements and generates the new iterable object
#it will take two arguments one is fun and iterableobject(list,string,tuple)


#out=list(map(function,iterable_obj))

#
# def square(a):
#     return a*a

#print("result :",square(5))

#x=list(range(1,11))
#print(x)
# out=list(map(square,x))
# # print("result :",out)
# out=list(map(lambda a:a*a,x))
# print("result :",out)

# reduce :  reduce fun redcuce the sequence of elements into a single element by applyijng reduce function
# if we want to use reduce fun u must import the module called functools

from functools import reduce

# resuce also take two args one is func, iterabelobject
# syntaax : reduce(function,iterable_obj)

# def reduce_ele(a,b):
#     return a+b
# # print("result :",reduce_ele(10,20))
# x=list(range(1,6)) # [1-10]

# out=reduce(reduce_ele,x)     # [1,2,3,4,5]  # 15
# print("out :",out)

# out=reduce(lambda a,b:a+b,x)
# print("result :",out)


# reursive function :  a function call itself is called recursive functio n

# es ex:
# x=1
# def python():
#     global x
#     if x!=6:
#        print("x val :",x)
#        x=x+1
#        python()
#     else:
#         return
#
# python()


# fact:
# import math
# print(math.factorial(4))


# def fact(n):
#     if n==0:
#         result=1
#     else:
#         result=n*fact(n-1)                           #3*(2)  #2*(1) # 1*(0)
#     return result
# print("factorial val :",fact(3))

# i,f=1,1
#
# def fact(n):
#     global f,i
#     if n==0:
#         return f
#     else:
#         f=f*i
#         i=i+1
#         fact(n-1)
#     return f
# print("fact :",fact(5))

# n    f   i     f=f*i
# 3    1    1    f=1*1=1
# 2      1    2  f=1*2=2
# 1     2     3   f=3*2=6
# 0

#  return :
# we can return for multiple purpose
# usin return we can come out from te function withh out any value or with value
# one function can hhave mutiple return statements
# value return
# control return

# def add(a,b):
#     return a+b
#
# out=add(10,20)
# print("add :",out)

# def hi():
#     print("Hi")
#     return 200
#     print("hhello")
#     print("student")
#
#     print("friend")
#     return 100
#
# out=hi()
# print("val :",out)

# return mutiple values fromj the function
# case 1 : return mutiplw values wile callingg  if we keep only one variable aall values will b stored in tuple format
# case 2 : if we want to store all retuen values in individual variables we jave to sepecify num of arguments based on return values
# def hi(n):
#     if n==1:
#         return n*10,n+2,n*5
#     else:
#         return n*3,n*n,n*2

# out=hi(2)
# print(out)

# a,b,c=hi(2)
# print("a val :",a)
# print("b val :",b)
# print("c val :"


tuple=[1,2,45,6,3,4,7]
gh=tuple.sort()
print(gh)


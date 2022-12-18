# oops -> object oriented programming system

# class -> collection of objects and methods n varibales
#class is a keyword

#syntax: "class keyword "Class name " :

#class A:
    #functions
    # variabls

# object -> object is blueprint of class
#Syntx : object name=A()
# we can create any num of objects to the class
# obj=A()
#
#
# #Ex:
#
#
#
# class A:
#     def python(self):
#         print("Python is good")
#     def java(self):
#         print("JAva is good")
# obj=A()
# obj.java()
# obj.python()
#
# class B:
#     def add(self):
#         print("addtion")
# obj=B()
# obj.add()
# obj.add()
# print(B.add())
# class A:
#     def python(self):
#         print("hello python")
# obj=A()
# obj.python()
# obj.java()

# method defenation:
#styntax:
# def methodname(self) # self is a default var



# class B:
#     def python(self):
#         print("HELO WORLD")
#     def java(self):
#         print("JAVA")
# obj1=B()
# obj1.python()
# obj2=B()
# obj2.java()

# x= {'1':['a','b'], '2':['c','d']} # ['ac','ad','bc','bd']
#
# a=x['1']
# b=x['2']
# print(a,b)
# out=[]
# for i in range(len(a)):    #a[i]=a
#      for j in range(len(b)):
#           temp=a[i]+b[j]
#           out.append(temp)
# print(out)
# out={}
#
# x={'A':[1,2,3],'B':[4,5,6]}
# keys=list(x.keys())
# val=list(x.values())
# for i in range(len(val)):
#     val[i].reverse()
# print(val)
# out=dict(zip(keys,val))
# print(out)

# print(keys)
# for i in x.keys():
#     x[i].reverse()
#     out[i]=x[i]
#     print(out)

# x='Hello PYTHON who ARE YOU' #{'H':'HELLO','P':'PYTHON','W':'WHO','A':'ARE','Y':'YOU'}
# x=x.upper()
# print(x)
# keys=[]
# values=[]
# x=x.split()
# for i in range(len(x)):
#     keys.append(x[i][0])
#     values.append(x[i])
# out=dict(zip(keys,values))
# print(out)






# x= {'1':['a','b'], '2':['c','d']} # ['ac','ad','bc','bd']
#
# a=x['1']
# b=x['2']
# print(a,b)
# out=[]
# for i in range(len(a)):    #a[i]=a
#      for j in range(len(b)):
#           temp=a[i]+b[j]
#           out.append(temp)
# print(out)
# out={}
#
# x={'A':[1,2,3],'B':[4,5,6]}
# keys=list(x.keys())
# val=list(x.values())
# for i in range(len(val)):
#     val[i].reverse()
# print(val)
# out=dict(zip(keys,val))
# print(out)

# print(keys)
# for i in x.keys():
#     x[i].reverse()
#     out[i]=x[i]
#     print(out)

# x='Hello PYTHON who ARE YOU' #{'H':'HELLO','P':'PYTHON','W':'WHO','A':'ARE','Y':'YOU'}
# x=x.upper()
# print(x)
# keys=[]
# values=[]
# x=x.split()
# for i in range(len(x)):
#     keys.append(x[i][0])
#     values.append(x[i])
# out=dict(zip(keys,values))
# print(out)



# class B:    # clss declaration
#     def python(self):       # instance methods
#         print("Python")
#     def java(self):
#         print("Java")
#     def C(self):
#         print("C lan")
# obj1=B()  # object creation for class
# obj1.python()
# obj1.java()
# obj1.C()

# self : self is a defaut varible which always pointing to the current obj
# self is useful for to access the instance methods of object and instance varibles
# sef is defaut argument and self is always the first parameter for instance methods

# we can crate n num of objects for the class


# class B:    # clss declaration
#     def python(self,a,b):       # instance methods
#         print("Python")
#         print(a)
#         print(b)
#     def java(self,a,b):       # instance methods
#         print("JAVA")
#         print(a)
#         print(b)
# obj1=B()   # object creation for class
# obj1.python(10,20)
# obj1.java("HELO",50)
# obj2=B()
# obj2.python(100,200)
# obj2.java(300,400)
#
# obj2=B()
# obj2.java(100,200)


# Constructor

# constryuctor is a special method in python
# the name constructor should be __init__(self) method
# syntx : def __init__(self)
# construtor wil execute automatically when we create object
# the main purpose of constructor is declare n inilise the varibles
# construtor wil b executed only once
# construtor wil take atleast one arg thats called self
#  construtor  is optional and if we not providing any constructor then python wil provide default constructor

# class A:
#     def __init__(self):
#         print("constructor")
# obj=A()
# obj1=A()
# obj2=A()
# obj3=A()

# class B:    # clss declaration
#     def __init__(self,x,y):  #   constructor
#          self.a=x
#          self.b=y
#          print("caling init method")
#          print(self.a)
#          print(self.b)
#     def python(self):       # instance methods
#         print("callinfg Python")
#         print(self.a)
#         print(self.b)
#
#     def java(self,a,b):
#         print('JAVA')
#         print(a)
#         print(b)
#         print(self.a)
#         print(self.b)


# x=int(input("Enter  x val :"))
# y=int(input("Enter  y val :"))
# obj1=B(x,y)  # object creation for class(10,20)
# obj1.python()
# obj1.java(100,200)
# obj1.python()
# obj1.python()

# diff b/w method nand constructor
# name of method can be anythig        ->  constructior name shoud b alwaysn __init__ method
# method will b executed whenever u    ->  constuctor will be executed automatically at the time of object cfreattion
# call method
# method can call n num of times        -> constructor will call only once per object
# inside the method we can write        -> inside the constructor we can declare and initlise the instance
# business loic




#   diff b/w method and construtor

# method name can b anything
# contructor name is alwys  __init__

# method can call any num of times
# construtor wil b executed only once per object

# method  will call if we call method
# construtor wil call automatically when object is creation

# inside method  we can write business logic
# inside contrutor we can declare and intilise the varibes

# obj2=B(x,y)
#obj1.python(10,20)

# class A:
#     def __init__(self,x,y):
#         self.a=x
#         self.b=y
#         print(self.a,self.b)
#     def sum(self):
#         return self.a+self.b
#     def mul(self):
#         return self.a*self.b
# obj=A(10,20)
# sum=obj.sum()
# print("Sum of two variables :",sum)
# mul=obj.mul()
# print("mul of two variables :",mul)

# class A:
#     def str_lower(self,a):
#         return a.lower()
#     def list_ele(self,x):  #['python','is','good']
#         return x.split()
# obj=A()
# sum=obj.str_lower('PYTHON')
# print("lower case:",sum)
# x='python is good'
# mul=obj.list_ele(x)
# print("list is :",mul)

#

# class B:
#     def __init__(self):
#         print("object is created")
#     def python(self,a,b):   #if there is a self in method u must call with obj ref
#         print("Python")
#         print(a)
#         print(b)
# obj1=B()
# obj1.python(10,20)
# B.python(obj1,10,20)

# create
#self  -> self is a deult variable  methods in the class in which is always pointing to the current object
# using self we can access instance methods and varible

#__int__(self)
#init method will call whenever u create object
#init method used fro intilise the varibles
# init mthod called as constructor
#using init method we can find how many objects r creted for the class
# init method dose not have return type
# atle
#
# class B:
#     def __init__(self,a,b):
#         print("object is created")
#         self.a=a
#         self.b=b
#         print("a val",self.a)
#         print("b vl",self.b)
#     def add(self):
#        print("add",self.a+self.b)
#     def mul(self):
#         print("mul",self.a*self.b)

# obj1=B(10,20)
# obj1.add()
# obj1.mul()
# print(obj1.a)
# print(obj1.b)
#B.mul(obj1)

# using init method we can find num of objects r created for perticuler class

# class B:
#     count=0
#     def __init__(self):
#         B.count=B.count+1
#         #print("num of objects are :",B.count)
#     def num_obj(self):
#         print("Num of objects r :",B.count)
#
# obj1=B()
# obj2=B()
# obj3=B()
# obj4=B()
# obj4.num_obj()


# create a class  which is having one init method and two objsts

# create a class  which is having one init method and intilise two variables and create instnce method (add) sum of two num


# types of variables

# instance var
# Static var
# local var

# instance: # the value of variable is verfied from object to object such type of varibles r clled instance varibes
# for every object saparate copy of instnce varibbles will be created

#where can we declare instance var

# inside the constrrutor using self
# inside the instance method
# out side the class using object ref
# instance var value can be chnaged any other instance method


class A:
    def __init__(self):
        self.a=100   # instance var
        print("init method ",self.a)
        #self.b=2000
    def python(self):  # instance method
        self.b=300
        print("inside instance method ",self.a)
        print("inside instance method ",self.b)
    def java(self):  # instance method
        self.b=1000
        print("inside java ", self.a)
        print("inside java",self.b)
    def C(self):
        print("inside C",self.b)
        print("outide var",self.c)

# obj=A()
# obj.c=2000
# obj.python()
# obj.java()
# obj.C()
# # print(obj.a)
# # print(obj.b)
# # print(obj.c)
# print(obj.__dict__)


# class B:
#     def __init__(self,x,y):
#         self.a=x
#         self.b=y
#         # print(self.a)
#         # print(self.b)
#     def python(self):
#         print(self.a)
#         print(self.b)
#
# obj=B(100,200)
# obj.python()
# obj1=B(1000,2000)
# obj1.python()



# static var
#
# the var which r defind inside the class but it should b outside of the methods in the class and if we want to define inside the methods using class name
# then we hav to define using classname
# where can we declare
# inside the constrctor using class name
# inside the instance method using class name
# inside the class method using class name or cls var
# inside the static method using class name
# we can use outside of the class using class ref

class A:
    x=10     # static or global
    def __init__(self):   # constrctor
        A.y=2000
        print("inside constructor :",A.x)
    def python(self):      # instance method
        A.z=1000
        print("inside instnce method ",A.z)
        print("inside instncemethod ",A.y)
        print("inside instance methid",A.x)


    @classmethod         # class method
    def java(cls):
        A.s=2000
        cls.c=500    # cls var or static var
        print("inside classmethod ",cls.c)
        print("inside classmethod ",A.s)
        print("x val :",A.x)
        print("x val",cls.x)
    @staticmethod       # static  method
    def print():
        A.d=5000
        print("inside  static method ",A.d)
        print("inside the static method X val",A.x)
# obj=A()
# obj.python()
# A.java()
# A.print()
# print(obj.__dict__)


# class A:
#     x=1000  # static var or cls var
#     def python(self):   # instance method  # we can access static or cls var using classname or self also
#         print("instanc :",self.x)
#         print("instance :",A.x)
#     @classmethod
#     def java(cls):    # we can access static var using class name or cls
#         print("class method :", cls.x)
#         print("class method :", A.x)
#     @staticmethod
#     def C():
#         print("Static method",A.x)
# obj=A()
# obj.python()
# A.java()
# A.C()


    # static var or class vr -> access in inside the instance method we can chnge the value but its applicable for only in that method itself using self and we can only read the val using self

# in class method  @class method -> using classname.varname or cls.var
# inside the static method -> using clasbnme.varnme  -> @staticmethod
# object not required for the static n clss method  but we can these methods using class ref
# static or clss var is the gobal varible for the all the methods inside the class

#
# class A:
#     x=10
#     def python(self):
#         self.x=100
#         print(A.x)
#         print(self.x)
#         #A.x=2000
#     @classmethod
#     def java(cls):
#         print(A.x)
#         print(cls.x)
#     @staticmethod
#     def C():
#         print(A.x)
# obj=A()
# obj.python()
# A.java()
# A.C()
# # obj.C()
# # print(obj.x)



# local var : the var which is defned inside the method is called and we can access inside the method only
# instance var  -> accessing using self applicable for all the instncee methods inside the class
# static/cls var -> we can abe to access all the methods here
# local var -> we can define and access only inside the method
# def naga():
#     print("HELLO")
#
# class A:
#     def python(self):
#         self.x=2000
#         a=200     # local var
#         print(self.x)
#         print(a)
#     def java(self):
#         print(self.x)
#         print()
# obj=A()
# obj.python()
# obj.java()

